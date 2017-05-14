#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python analysis_source.py "../Www/Hacking/"
# Educational purpose only !

# TODO:
# 1. https://www.ripstech.com/blog/2017/why-mail-is-dangerous-in-php/
# 2. Parcourir les fichiers en recursif avec les includes et afficher toutes les modifications de la variable

import sys, getopt
import os, re


score = 0
payloads   = [
  # /!\ Detection Format (.*)function($vuln)(.*)
  # Function_Name:String, Vulnerability_Name:String, Protection:Array
  ["eval","Remote Command Execution",["escapeshellarg","escapeshellcmd"]],
  ["popen","Remote Command Execution",["escapeshellarg","escapeshellcmd"]],
  ["system","Remote Command Execution",["escapeshellarg","escapeshellcmd"]],
  ["passthru","Remote Command Execution",["escapeshellarg","escapeshellcmd"]],
  ["exec","Remote Command Execution",["escapeshellarg","escapeshellcmd"]],
  ["shell_exec","Remote Command Execution",["escapeshellarg","escapeshellcmd"]],

  ["include","File Inclusion",[]],
  ["require","File Inclusion",[]],
  ["include_once","File Inclusion",[]],
  ["require_once","File Inclusion",[]],
  ["readfile","File Inclusion",[]],
  ["file_get_contents","File Inclusion",[]],

  ["mysql_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysql_unbuffered_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysql_db_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli::real_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli_real_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli::query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli_query","SQL Injection",["mysql_real_escape_string"]],
  # pdo querys

  ["move_uploaded_file","File Upload",[]],

  ["echo","Cross Site Scripting",["htmlentities","htmlspecialchars"]],

  # Print etc
  ["mail", "Insecure E-mail",[]]
]

# Display the found vulnerability with basic informations like the line
def display(path,payload,vulnerability,line,declaration_text,declaration_line):

	# New Vulnerability found -> Score +1
	global score
	score = score+1

	print  "-"*60+"\r\n\033[1m"+"Potential vulnerability found : \033[0m\033[92m" + payload[1]+"\033[0m"
	print  "\033[1mLine \033[0m\033[92m"+line+"\033[0m in "+path

	if not "POST" in vulnerability[1] and not "GET" in vulnerability[1]:
		print  "\033[1mCode : \033[0m"+payload[0]+'('+vulnerability[0]+"\033[93m"+vulnerability[1]+"\033[0m"+vulnerability[2]+')'
		if declaration_text != "":
			print "\033[1mDeclared at line \033[0;92m"+declaration_line+"\033[0m : "+ declaration_text
		else:
			print "\033[1mUndeclared \033[0m"+ declaration_text+" in the file"
	else:
		print  "\033[1mCode : \033[0m"+payload[0]+'('+vulnerability[0]+"\033[93m"+vulnerability[1]+"\033[0m"+vulnerability[2]+')'


# Find the line where the vulnerability is located
def find_line_vuln(path,payload,vulnerability,content):
	content = content.split('\n')
	for i in range(len(content)):
		if payload[0]+'('+vulnerability[0]+vulnerability[1]+vulnerability[2]+')' in content[i]:
			return str(i)
	return "-1"


# Find the line where the entry point is declared
def find_line_declaration(declaration, content):
	content = content.split('\n')
	for i in range(len(content)):
		if declaration in content[i]:
			return str(i)
	return "-1"


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



if __name__ == "__main__":

	# Handle arguments
	url = sys.argv[1]
	if len(sys.argv) < 2:
		print 'Usage : main.py "./link/to/somewhere"'
		exit()

	print "-"*60+"\r\n\033[1mAnalyzing '"+url+"' source code\033[0m"

	# Analyse a file or an entire folder
	if(os.path.isfile(url)):
		analysis(url)
	else:
		recursive(url,0)

	# Display final result
	if score != 0:
		print "-"*60+"\r\n\r\033[0mApplication score : \033[91m"+str(score)+" potential vulnerabilities found !\033[0m\r\n"+"-"*60
	else:
		print "-"*60+"\r\n\r\033[0mApplication score : \033[92m"+str(score)+" potential vulnerabilities found !\033[0m\r\n"+"-"*60
