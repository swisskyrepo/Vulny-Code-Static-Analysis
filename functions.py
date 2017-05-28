#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *

# Display the found vulnerability with basic informations like the line
def display(path,payload,vulnerability,line,declaration_text,declaration_line, colored):

	# Potential vulnerability found :  SQL Injection
	header = "\033[1mPotential vulnerability found : \033[92m{}\033[0m".format(payload[1])

	# Line  25  in test/sqli.php
	line = "n°\033[92m{}\033[0m in {}".format(line,path)

	# Code : include($_GET['patisserie'])
	vuln = ("".join(vulnerability)).replace(colored, "\033[93m"+colored+"\033[0m")
	vuln = "{}({})".format(payload[0], vuln)

	# Final Display
	rows, columns = os.popen('stty size', 'r').read().split()
	print "-" * (int(columns)-1)
	print "Name        " + "\t"+header
	print "-" * (int(columns)-1)
	print "\033[1mLine \033[0m        " + "\t"+line
	print "\033[1mCode \033[0m        " + "\t"+vuln

	# Declared at line 1 : $dest = $_GET['who'];
	declared = ""
	if not "$_" in colored:
		if declaration_text != "":
			declared = "Line n°\033[0;92m"+declaration_line+"\033[0m : "+ declaration_text
		else:
			declared = "Undeclared \033[0m"+ declaration_text+" in the file"
		print "\033[1mDeclaration \033[0m " + "\t"+declared

	# Small delimiter
	print ""

# Find the line where the vulnerability is located
def find_line_vuln(path,payload,vulnerability,content):
	content = content.split('\n')
	for i in range(len(content)):
		if payload[0]+'('+vulnerability[0]+vulnerability[1]+vulnerability[2]+')' in content[i]:
			return str(i-1)
	return "-1"


# Find the line where the entry point is declared
# TODO: should be an array of the declaration and modifications
def find_line_declaration(declaration, content):
	content = content.split('\n')
	for i in range(len(content)):
		if declaration in content[i]:
			return str(i)
	return "-1"


# Format the source code in order to improve the detection
def clean_source_and_format(content):
    # Clean up - replace tab by space
    content = content.replace("	"," ")

    # Quickfix to detect both echo("something") and echo "something"
    content = content.replace("echo ","echo(")
    content = content.replace(";",");")
    return content

# Check the line to detect an eventual protection
def check_protection(payload, match):
    for protection in payload:
        if protection in "".join(match):
            return True
    return False

# Check exception - When it's a function($SOMETHING) Match declaration $SOMETHING = ...
def check_exception(match):
    exceptions = ["_GET","_REQUEST","_POST","_COOKIES","_FILES"]
    is_exception = False
    for exception in exceptions:
        if exception in match:
            return True
    return False

# Check declaration
def check_declaration(content, vuln, path):
    # Follow and parse include, then add it's content
    regex_declaration = re.compile("(include.*?|require.*?)\([\"\'](.*?)[\"\']\)")
    includes          = regex_declaration.findall(content)
	# Path is the path of the current scanned file, we can use it to compute the relative include
    for include in includes:
		relative_include = os.path.dirname(path)+"/"
		path_include     = relative_include + include[1]
		with open(path_include, 'r') as f:
			content = f.read() + content

	# Extract declaration
    regex_declaration = re.compile("\$"+vuln[1:]+"([\t ]*)=(?!=)(.*)")
    declaration       = regex_declaration.findall(content)
    if len(declaration)>0:

		# Check constant then return True if constant because it's false positive
		declaration_text = "$"+vuln[1:] +declaration[0][0]+"="+declaration[0][1]
		line_declaration = find_line_declaration(declaration_text, content)
		regex_constant = re.compile("\$"+vuln[1:]+"([\t ]*)=[\t ]*?([\"\'(]*?[a-zA-Z0-9{}_\(\)@\.: ]*?[\"\')]*?);")
		false_positive = regex_constant.match(declaration_text)

		if false_positive:
			return (True, "","")
		return (False, declaration_text,line_declaration)

    return (False, "","")
