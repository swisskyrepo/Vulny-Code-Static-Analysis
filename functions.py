#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from indicators import *


# Display the found vulnerability with basic informations like the line
def display(path,payload,vulnerability,line,declaration_text,declaration_line):
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
