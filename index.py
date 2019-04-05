#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python index.py --dir test
# Educational purpose only !

# TODO afficher toutes les modifications de la variable

import sys
import argparse
import os, re
from detection import *
from indicators import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', action ='store', dest='dir', help="Directory to analyse")
    parser.add_argument('--plain', action ='store_true', dest='plain', help="No color in output")
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
        print ("\n\033[{}mAnalyzing '{}' source code\033[{}m".format('0' if results.plain else '1', results.dir, '0'))

        if os.path.isfile(results.dir):
            analysis(results.dirm, results.plain)
        else:
            recursive(results.dir,0, results.plain)
        scanresults()

    else:
        parser.print_help()
