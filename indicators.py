#!/usr/bin/python
# -*- coding: utf-8 -*-

payloads = [
  # /!\ Detection Format (.*)function($vuln)(.*)

  # Function_Name:String, Vulnerability_Name:String, Protection_Function:Array
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
