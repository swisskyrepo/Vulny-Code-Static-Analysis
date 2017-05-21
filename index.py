#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python index.py --dir test
# Educational purpose only !

# TODO remonter les includes (parse include/require xxx , chercher son contenu et l'ajouter au debut du content actuel)
# TODO afficher toutes les modifications de la variable -
# TODO enlever les faux positifs : constantes
# BUG variable multiple
# BUG color var['something']

import sys
import argparse
import os, re
from detection import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', action ='store', dest='dir', help="Directory to analyse")
    results = parser.parse_args()

    if results.dir != None:
        print "-"*60+"\r\n\033[1mAnalyzing '"+results.dir+"' source code\033[0m"

        if os.path.isfile(results.dir):
            analysis(results.dir)
        else:
            recursive(results.dir,0)
