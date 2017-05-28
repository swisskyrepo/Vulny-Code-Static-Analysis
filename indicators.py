#!/usr/bin/python
# -*- coding: utf-8 -*-

# /!\ Detection Format (.*)function($vuln)(.*) matched by payload[0]+regex_indicators
regex_indicators = '\((.*?)(\$_GET\[.*?\]|\$_FILES\[.*?\]|\$_POST\[.*?\]|\$_REQUEST\[.*?\]|\$_COOKIES\[.*?\]|\$_SESSION\[.*?\]|\$(?!this|e-)[a-zA-Z0-9_]*)(.*?)\)'

# Function_Name:String, Vulnerability_Name:String, Protection_Function:Array
payloads = [
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

  ["show_source","File Inclusion / Path Traversal",[]],
  ["highlight_file","File Inclusion / Path Traversal",[]],

  ["mysql_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysql_unbuffered_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysql_db_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli::real_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli_real_query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli::query","SQL Injection",["mysql_real_escape_string"]],
  ["mysqli_query","SQL Injection",["mysql_real_escape_string"]],
  ["->query","SQL Injection",["->prepare"]],
  ["->exec","SQL Injection",["->prepare"]],
  ["->execute","SQL Injection",["->prepare"]],

  ["move_uploaded_file","File Upload",[]],

  ["echo","Cross Site Scripting",["htmlentities","htmlspecialchars"]],
  ["print","Cross Site Scripting",["htmlentities","htmlspecialchars"]],

  ["mail", "Insecure E-mail",[]],

  ["unserialize", "PHP Object Injection",[]]
]
