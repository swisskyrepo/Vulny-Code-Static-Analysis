#!/usr/bin/env bash

echo "Generating report"
mkdir Report 2> /dev/null
python index.py --dir $1 --plain > Report/exported.txt
cat Report/exported.txt | grep "Remote Co" -A4 > Report/RemoteCodeExecution.txt
cat Report/exported.txt | grep "File Inclusion" -A4 > Report/File_Inclusion.txt
cat Report/exported.txt | grep "SQL Injection" -A4 > Report/SQL_Injection.txt
cat Report/exported.txt | grep "File Upload" -A4 > Report/File_Upload.txt
cat Report/exported.txt | grep "Cross Site Scripting" -A4 > Report/Cross_Site_Scripting.txt
cat Report/exported.txt | grep "XPATH Injection" -A4 > Report/XPATH_Injection.txt
cat Report/exported.txt | grep "LDAP Injection" -A4 > Report/LDAP_Injection.txt
cat Report/exported.txt | grep "Insecure E-mail" -A4 > Report/Insecure_E-mail.txt
cat Report/exported.txt | grep "PHP Object Injection" -A4 > Report/PHP_Object_Injection.txt
cat Report/exported.txt | grep "Header Injection" -A4 > Report/Header_Injection.txt
cat Report/exported.txt | grep "URL Redirection" -A4 > Report/URL_Redirection.txt
cat Report/exported.txt | grep "Hardcoded Credential" -A4 > Report/Hardcoded_Credential.txt


echo "Found :"
ls -ail Report
