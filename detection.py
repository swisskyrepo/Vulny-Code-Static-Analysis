#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *
from functions import *

result_count = 0
result_files = 0


# Analyse the source code of a single page
def analysis(path, plain):
    global result_files
    result_files += 1
    with open(path, 'r') as content_file:

        # Clean source for a better detection
        content = content_file.read()
        content = clean_source_and_format(content)

        # Hardcoded credentials (work as an exception, it's not function based)
        credz = ['pass', 'secret', 'token', 'pwd']
        for credential in credz:

            content_pure = content.replace(' ', '')
            regex = re.compile("\$" + credential + ".*?=[\"|'][^\$]+[\"|']", re.I)
            matches = regex.findall(content_pure)

            # If we find a variable with a constant for a given indicator
            for vuln_content in matches:
                payload = ["", "Hardcoded Credential", []]

                # Get the line
                line_vuln = -1
                splitted_content = content.split('\n')
                for i in range(len(splitted_content)):
                    regex = re.compile("\$" + credential + ".*?=", re.I)
                    matches = regex.findall(splitted_content[i])
                    if len(matches) > 0:
                        line_vuln = i

                declaration_text = vuln_content
                line_declaration = str(line_vuln)
                occurence = 1

                display(path, payload, vuln_content, line_vuln, declaration_text, line_declaration, vuln_content, occurence, plain)

        # Detection of RCE/SQLI/LFI/RFI/RFU/XSS/...
        for payload in payloads:
            regex = re.compile(payload[0] + regex_indicators)
            matches = regex.findall(content)

            for vuln_content in matches:
                occurence = 0

                # Security hole detected, is it protected ?
                if check_protection(payload[2], vuln_content) == False:
                    declaration_text, line_declaration = "", ""

                    # Managing multiple variable in a single line/function
                    sentence = "".join(vuln_content)
                    regax = re.compile(regex_indicators[2:-2])
                    for vulnerable_var in regax.findall(sentence):
                        false_positive = False
                        occurence += 1

                        # No declaration for $_GET, $_POST ...
                        if check_exception(vulnerable_var[1]) == False:
                            # Look for the declaration of $something = xxxxx
                            false_positive, declaration_text, line_declaration = check_declaration(content, vulnerable_var[1], path)

                            # Set false positive if protection is in the variable's declaration
                            false_positive = false_positive or check_protection(payload[2], declaration_text) == True

                        # Display all the vuln
                        line_vuln = find_line_vuln(path, payload, vuln_content, content)

                        # Check for not $dest="constant"; $dest='cste'; $dest=XX;
                        if not "$_" in vulnerable_var[1]:
                            if not "$" in declaration_text.replace(vulnerable_var[1], ''):
                                false_positive = True

                        if not false_positive:
                            global result_count
                            result_count = result_count + 1
                            display(path, payload, vuln_content, line_vuln, declaration_text, line_declaration, vulnerable_var[1], occurence, plain)


# Run thru every files and subdirectories
def recursive(dir, progress, plain):
    progress += 1
    progress_indicator = '⬛'
    if plain: progress_indicator = "█"
    try:
        for name in os.listdir(dir):

            print('\tAnalyzing : ' + progress_indicator * progress + '\r'),

            # Targetting only PHP Files
            if os.path.isfile(os.path.join(dir, name)):
                if ".php" in os.path.join(dir, name):
                    analysis(dir + "/" + name, plain)
            else:
                recursive(dir + "/" + name, progress, plain)

    except OSError as e:
        print
        "Error 404 - Not Found, maybe you need more right ?" + " " * 30
        exit(-1)


# Display basic informations about the scan
def scanresults():
    global result_count
    global result_files
    print("Found {} vulnerabilities in {} files".format(result_count, result_files))
