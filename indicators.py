#!/usr/bin/python
# -*- coding: utf-8 -*-

# /!\ Detection Format (.*)function($vuln)(.*) matched by payload[0]+regex_indicators
regex_indicators = '\\((.*?)(\\$_GET\\[.*?\\]|\\$_FILES\\[.*?\\]|\\$_POST\\[.*?\\]|\\$_REQUEST\\[.*?\\]|\\$_COOKIES\\[.*?\\]|\\$_SESSION\\[.*?\\]|\\$(?!this|e-)[a-zA-Z0-9_,]*)(.*?)\\)'

# Function_Name:String, Vulnerability_Name:String, Protection_Function:Array
payloads = [

    # Remote Command Execution
    ["eval", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["popen", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["system", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["passthru", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["exec", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["shell_exec", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["pcntl_exec", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["assert", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["proc_open", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["expect_popen", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["create_function", "Remote Command Execution", ["escapeshellarg", "escapeshellcmd"]],
    ["call_user_func", "Remote Code Execution", []],
    ["call_user_func_array", "Remote Code Execution", []],
    ["preg_replace", "Remote Command Execution", ["preg_quote"]],
    ["ereg_replace", "Remote Command Execution", ["preg_quote"]],
    ["eregi_replace", "Remote Command Execution", ["preg_quote"]],
    ["mb_ereg_replace", "Remote Command Execution", ["preg_quote"]],
    ["mb_eregi_replace", "Remote Command Execution", ["preg_quote"]],

    # File Inclusion / Path Traversal
    ["virtual", "File Inclusion", []],
    ["include", "File Inclusion", []],
    ["require", "File Inclusion", []],
    ["include_once", "File Inclusion", []],
    ["require_once", "File Inclusion", []],

    ["readfile", "File Inclusion / Path Traversal", []],
    ["file_get_contents", "File Inclusion / Path Traversal", []],
    ["stream_get_contents", "File Inclusion / Path Traversal", []],
    ["show_source", "File Inclusion / Path Traversal", []],
    ["fopen", "File Inclusion / Path Traversal", []],
    ["file", "File Inclusion / Path Traversal", []],
    ["fpassthru", "File Inclusion / Path Traversal", []],
    ["gzopen", "File Inclusion / Path Traversal", []],
    ["gzfile", "File Inclusion / Path Traversal", []],
    ["gzpassthru", "File Inclusion / Path Traversal", []],
    ["readgzfile", "File Inclusion / Path Traversal", []],

    # MySQL(i) SQL Injection
    ["mysql_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli_multi_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli_send_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli_master_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli_master_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysql_unbuffered_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysql_db_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli::real_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli_real_query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli::query", "SQL Injection", ["mysql_real_escape_string"]],
    ["mysqli_query", "SQL Injection", ["mysql_real_escape_string"]],

    # PostgreSQL Injection
    ["pg_query", "SQL Injection", ["pg_escape_string", "pg_pconnect", "pg_connect"]],
    ["pg_send_query", "SQL Injection", ["pg_escape_string", "pg_pconnect", "pg_connect"]],

    # SQLite SQL Injection
    ["sqlite_array_query", "SQL Injection", ["sqlite_escape_string"]],
    ["sqlite_exec", "SQL Injection", ["sqlite_escape_string"]],
    ["sqlite_query", "SQL Injection", ["sqlite_escape_string"]],
    ["sqlite_single_query", "SQL Injection", ["sqlite_escape_string"]],
    ["sqlite_unbuffered_query", "SQL Injection", ["sqlite_escape_string"]],

    # PDO SQL Injection
    ["->arrayQuery", "SQL Injection", ["->prepare"]],
    ["->query", "SQL Injection", ["->prepare"]],
    ["->queryExec", "SQL Injection", ["->prepare"]],
    ["->singleQuery", "SQL Injection", ["->prepare"]],
    ["->querySingle", "SQL Injection", ["->prepare"]],
    ["->exec", "SQL Injection", ["->prepare"]],
    ["->execute", "SQL Injection", ["->prepare"]],
    ["->unbufferedQuery", "SQL Injection", ["->prepare"]],
    ["->real_query", "SQL Injection", ["->prepare"]],
    ["->multi_query", "SQL Injection", ["->prepare"]],
    ["->send_query", "SQL Injection", ["->prepare"]],

    # Cubrid SQL Injection
    ["cubrid_unbuffered_query", "SQL Injection", ["cubrid_real_escape_string"]],
    ["cubrid_query", "SQL Injection", ["cubrid_real_escape_string"]],

    # MSSQL SQL Injection : Warning there is not any real_escape_string
    ["mssql_query", "SQL Injection", ["mssql_escape"]],

    # File Upload
    ["move_uploaded_file", "File Upload", []],

    # Cross Site Scripting
    ["echo", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["print", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["printf", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["vprintf", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["trigger_error", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["user_error", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["odbc_result_all", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["ifx_htmltbl_result", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["die", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],
    ["exit", "Cross Site Scripting", ["htmlentities", "htmlspecialchars"]],

    # XPATH and LDAP
    ["xpath", "XPATH Injection", []],
    ["ldap_search", "LDAP Injection", ["Zend_Ldap", "ldap_escape"]],

    # Insecure E-Mail
    ["mail", "Insecure E-mail", []],

    # PHP Objet Injection
    ["unserialize", "PHP Object Injection", []],

    # Header Injection
    ["header", "Header Injection", []],
    ["HttpMessage::setHeaders", "Header Injection", []],
    ["HttpRequest::setHeaders", "Header Injection", []],

    # URL Redirection
    ["http_redirect", "URL Redirection", []],
    ["HttpMessage::setResponseCode", "URL Redirection", []],

    # Server Side Template Injection
    ["->render", "Server Side Template Injection", []],
    ["->assign", "Server Side Template Injection", []],

    # Weak Cryptographic Hash
    ["md5", "Weak Cryptographic Hash", []],

    # Insecure Weak Random
    ["mt_rand", "Insecure Weak Random", []],
    ["srand", "Insecure Weak Random", []],
    ["uniqid", "Insecure Weak Random", []],

    # Information Leak
    ["phpinfo", "Information Leak", []],
    ["show_source", "Information Leak", []],
    ["highlight_file", "Information Leak", []],


]
