#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *


# Display the found vulnerability with basic informations like the line
def display(path,payload,vulnerability,line,declaration_text,declaration_line):
	print  "-"*80

	# Potential vulnerability found :  SQL Injection
	print ("\033[1mPotential vulnerability found : \033[92m%s\033[0m")%(payload[1])

	# Line  25  in test/sqli.php
	print  ("\033[1mLine \033[0m\033[92m%s\033[0m in %s")%(line,path)

	# Code : include($_GET['patisserie'])
	vuln = vulnerability[0]+"\033[93m"+vulnerability[1]+"\033[0m"+vulnerability[2]
	print ("\033[1mCode : \033[0m%s(%s)") % (payload[0], vuln)

	# Declared at line 1 : $dest = $_GET['who'];
	if not "$_" in vulnerability[1]:
		if declaration_text != "":
			print "\033[1mDeclared at line \033[0;92m"+declaration_line+"\033[0m : "+ declaration_text
		else:
			print "\033[1mUndeclared \033[0m"+ declaration_text+" in the file"




# Find the line where the vulnerability is located
def find_line_vuln(path,payload,vulnerability,content):
	content = content.split('\n')
	for i in range(len(content)):
		if payload[0]+'('+vulnerability[0]+vulnerability[1]+vulnerability[2]+')' in content[i]:
			return str(i)
	return "-1"


# Find the line where the entry point is declared
# TODO: should be an array of the declaration and modifications
def find_line_declaration(declaration, content):
	content = content.split('\n')
	for i in range(len(content)):
		if declaration in content[i]:
			return str(i)
	return "-1"
