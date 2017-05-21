#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python analysis_source.py "../Www/Hacking/"
# Educational purpose only !

# TODO
# 1. https://www.ripstech.com/blog/2017/why-mail-is-dangerous-in-php/
# 2. Parcourir les fichiers en recursif avec les includes et afficher toutes les modifications de la variable - detecter les constantes
# BUG du echo()

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
