#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python index.py --dir test
# Educational purpose only !

# TODO afficher toutes les modifications de la variable -
# BUG variable multiple (check en recursif dans vuln)
# BUG color var['something']
# BUG detection include
# BUG SQLi 2 ligne 17 not found
# TODO print help if no dir in arg

import sys
import argparse
import os, re
from detection import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', action ='store', dest='dir', help="Directory to analyse")
    results = parser.parse_args()

    if results.dir != None:
        print "      (`-')                    <-. (`-')_                                _(`-')    (`-')  _"
        print "     _(OO )     .->      <-.      \( OO) )     .->   _             .->  ( (OO ).-> ( OO).-/"
        print ",--.(_/,-.\,--.(,--.   ,--. )  ,--./ ,--/  ,--.'  ,-.\-,-----.(`-')----. \    .'_ (,------."
        print "\   \ / (_/|  | |(`-') |  (`-')|   \ |  | (`-')'.'  / |  .--./( OO).-.  ''`'-..__) |  .---'"
        print " \   /   / |  | |(OO ) |  |OO )|  . '|  |)(OO \    / /_) (`-')( _) | |  ||  |  ' |(|  '--."
        print "_ \     /_)|  | | |  \(|  '__ ||  |\    |  |  /   /) ||  |OO ) \|  |)|  ||  |  / : |  .--'"
        print "\-'\   /   \  '-'(_ .' |     |'|  | \   |  `-/   /` (_'  '--'\  '  '-'  '|  '-'  / |  `---."
        print "    `-'     `-----'    `-----' `--'  `--'    `--'      `-----'   `-----' `------'  `------'"
        print "                                                            Copyright @pentest_swissky     "
        print "\n\033[1mAnalyzing '"+results.dir+"' source code\033[0m"

        if os.path.isfile(results.dir):
            analysis(results.dir)
        else:
            recursive(results.dir,0)

    # else print help
