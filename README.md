# VulnyCode - PHP Code Static Analysis

[![Python 3.4+](https://img.shields.io/badge/python-3.4+-blue.svg)](https://www.python.org/downloads/release/python-360/)

Basic script to detect vulnerabilities into a PHP source code, it is using Regular Expression to find sinkholes.

```bash
╭─ 👻 swissky@crashlab: ~/Github/PHP_Code_Static_Analysis  ‹master*›
╰─$ python index.py --dir test    
------------------------------------------------------------
Analyzing 'test' source code
------------------------------------------------------------
Potential vulnerability found : File Inclusion
Line 19 in test/include.php
Code : include($_GET['patisserie'])
------------------------------------------------------------
Potential vulnerability found : Insecure E-mail
Line 2 in test/mail.php
Code : mail($dest, "subject", "message", "", "-f" . $_GET['from'])
Declared at line 1 : $dest = $_GET['who'];
```

Currently detecting :
 - SQL injection
 - Local File Inclusion
 - Insecure emails
 - Cross Site Scripting
 - Remote Commands Execution
 - LDAP injection
 - XPATH injection
 - PHP Objet Injection
 - Header injection
 - URL redirection
 - Hardcoded credential
 - High Entropy string

> if you want to export each vulnerabilities type into a folder use the "export.sh"

Don't forget to read the [license](/LICENSE) ;)
