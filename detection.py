#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *
from functions import *

# Analyse the source code of a single page
def analysis(path):
  with open(path, 'r') as content_file:
    content = content_file.read()

    # Clean source for a better detection
    content = content.replace("echo ","echo(")
    content = content.replace("; ",";)")

    # Detection of RCE/SQLI/LFI/RFI/RFU/XSS
    for payload in payloads:
      regex = re.compile(payload[0]+'\((.*?)(\$_GET\[.*\]|\$_FILES\[.*\]|\$_POST\[.*\]|\$_REQUEST\[.*\]|\$_COOKIES\[.*\]|\$_SESSION\[.*\]|\$(?!this|e-)[a-zA-Z0-9_]*)(.*)\)')
      matches = regex.findall(content)
      for match in matches:

      	# Detection of good protection
      	is_protected = False
      	for protection in payload[2]:
      		if protection in "".join(match):
      			is_protected = True

      	# Detect line of the vuln
      	if is_protected == False:

      		# When it's a function($SOMEHTING) Match declaration $SOMETHING = ...
      		exceptions = ["_GET","_REQUEST","_POST","_COOKIES","_FILES"]
      		is_exception = False
      		for exception in exceptions:
      			if exception in match[1]:
      				is_exception = True

      		declaration_text = ""
      		line_declaration = ""
      		if is_exception == False:
      			regex_declaration = re.compile("\$"+match[1][1:]+"([\t ]*)=(?!=)(.*)")
      			declaration = regex_declaration.findall(content)
      			if len(declaration)>0:
      				declaration_text = "$"+match[1][1:] +declaration[0][0]+"="+declaration[0][1]
      				line_declaration = find_line_declaration(declaration_text, content)

      		# Display all the informations
      		line_vuln = find_line_vuln(path,payload,match,content)
      		display(path,payload,match,line_vuln,declaration_text,line_declaration)


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
