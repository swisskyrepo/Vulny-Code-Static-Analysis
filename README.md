# VulnyCode - PHP Code Static Analysis [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=VulnyCode%20-%20PHP%20Code%20Static%20Analysis&url=https://github.com/swisskyrepo/Vulny-Code-Static-Analysis)

![1.0.0](https://img.shields.io/badge/Version-1.0.0%20Beta-RED) ![Python](https://img.shields.io/badge/Python-3.4+-GREEN) ![Platform](https://img.shields.io/badge/Platforms-Linux%20x64-yellowgreen) 

Basic script to detect vulnerabilities into a PHP source code, it is using Regular Expression to find sinkholes.

```bash
# HELP
╭─ 👻 swissky@crashlab: ~/Github/PHP_Code_Static_Analysis  ‹master*›
╰─$ python3 index.py           
usage: index.py [-h] [--dir DIR] [--plain]

optional arguments:
  -h, --help  show this help message and exit
  --dir DIR   Directory to analyse
  --plain     No color in output

# Example
╭─ 👻 swissky@crashlab: ~/Github/PHP_Code_Static_Analysis  ‹master*›
╰─$ python3 index.py --dir test    
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
- Arbitrary Cookie
- Arbitrary File Deletion
- Arbitrary Variable Overwrite
- Cross Site Scripting
- File Inclusion
- File Inclusion / Path Traversal
- File Upload
- Header Injection
- Information Leak
- Insecure E-mail
- Insecure Weak Random
- LDAP Injection
- PHP Object Injection
- Remote Code Execution
- Remote Command Execution
- Server Side Request Forgery
- Server Side Template Injection
- SQL Injection
- URL Redirection
- Weak Cryptographic Hash
- XML external entity
- XPATH Injection
- Hardcoded credentials
- High Entropy string

> if you want to export each vulnerabilities type into a folder use the "export.sh"

Don't forget to read the [license](/LICENSE) ;)


## Alternatives

* [RIPS - A static source code analyser for vulnerabilities in PHP scripts](https://blog.ripstech.com/2016/introducing-the-rips-analysis-engine/)
* [Cobra - Source Code Security Audit](https://github.com/WhaleShark-Team/cobra)
* [PHP parser written in Python using PLY](https://github.com/viraptor/phply)
* [Psalm - A static analysis tool for finding errors in PHP applications](https://psalm.dev/docs/security_analysis/)