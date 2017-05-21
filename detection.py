#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *
from functions import *

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

# Analyse the source code of a single page
def analysis(path):
  with open(path, 'r') as content_file:
    content = content_file.read()

    # Clean source for a better detection
    content = clean_source_and_format(content)

    # Detection of RCE/SQLI/LFI/RFI/RFU/XSS
    for payload in payloads:
      regex   = re.compile(payload[0]+regex_indicators)
      matches = regex.findall(content)
      for vuln in matches:

      	# Vulnerability detected
      	if check_protection(payload[2], vuln) == False:
      		declaration_text = ""
      		line_declaration = ""

      		if check_exception(vuln[1]) == False:

      			regex_declaration = re.compile("\$"+vuln[1][1:]+"([\t ]*)=(?!=)(.*)")
      			declaration = regex_declaration.findall(content)
      			if len(declaration)>0:
      				declaration_text = "$"+vuln[1][1:] +declaration[0][0]+"="+declaration[0][1]
      				line_declaration = find_line_declaration(declaration_text, content)

      		# Display all the informations
      		line_vuln = find_line_vuln(path, payload, vuln, content)
      		display(path, payload, vuln, line_vuln, declaration_text, line_declaration)


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
