#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *
from functions import *


# Analyse the source code of a single page
def analysis(path):
  with open(path, 'r') as content_file:

    # Clean source for a better detection
    content = content_file.read()
    content = clean_source_and_format(content)

    # Detection of RCE/SQLI/LFI/RFI/RFU/XSS
    for payload in payloads:
      regex   = re.compile(payload[0]+regex_indicators)
      matches = regex.findall(content)

      for vuln_content in matches:
        # Security hole detected, is it protected ?
      	if check_protection(payload[2], vuln_content) == False:
            declaration_text, line_declaration = "",""

            # Managing multiple variable in a single line/function
            sentence = "".join(vuln_content)
            regax = re.compile(regex_indicators[2:-2])
            for vulnerable_var in regax.findall(sentence):
                false_positive = False

                # BUG nt des var et mettre en couleur la bonne plutôt que la première
                # BUG ex fct(occurence) et mettre en couleur la xieme occurence
                # No declaration for $_GET, $_POST ...
                if check_exception(vulnerable_var[1]) == False:
                    # Look for the declaration of $something = xxxxx
                    false_positive, declaration_text, line_declaration = check_declaration(content, vulnerable_var[1], path)

                # Set false positive if protection is in the variable's declaration
                false_positive = false_positive or check_protection(payload[2], declaration_text)==True

                # Display all the vuln
                line_vuln = find_line_vuln(path, payload, vuln_content, content)
                if not false_positive:
                    display(path, payload, vuln_content, line_vuln, declaration_text, line_declaration, vulnerable_var[1])


# Run thru every files and subdirectories
def recursive(dir,progress):
  progress += 1
  try:
  	for name in os.listdir(dir):
  		print('\tAnalyzing : '+'⬛'*progress+'\r'),

  		# Targetting only PHP Files
  		if os.path.isfile(os.path.join(dir, name)):
  			if ".php" in os.path.join(dir, name):
  				analysis(dir+"/"+name)
  		else :
  			recursive(dir+"/"+name, progress)

  except OSError, e:
  	print "Error 404 - Not Found, maybe you need more right ?"+" "*30
  	exit(-1)
