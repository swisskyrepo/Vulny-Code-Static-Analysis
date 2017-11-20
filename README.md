# PHP_Code_Static_Analysis
Basic script to detect vulnerabilities into a PHP source code
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
 - Header injection
 - URL redirection
 - Hardcoded credential

> if you want to export each vulnerabilities type into a folder use the "export.sh"

Don't forget to read the [license](/LICENSE) ;)
