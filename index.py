#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author     : Swissky
# How to use : python index.py --dir test
# Educational purpose only !

# TODO afficher toutes les modifications de la variable

import argparse
from detection import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', action='store', dest='dir', help="Directory to analyse")
    parser.add_argument('--plain', action='store_true', dest='plain', help="No color in output")
    results = parser.parse_args()

    if results.dir is not None:
        print("""      (`-')                    <-. (`-')_                                _(`-')    (`-')  _
             _(OO )     .->      <-.      \\( OO) )     .->   _             .->  ( (OO ).-> ( OO).-/
        ,--.(_/,-.\\,--.(,--.   ,--. )  ,--./ ,--/  ,--.'  ,-.\\-,-----.(`-')----. \\    .'_ (,------.
        \\   \\ / (_/|  | |(`-') |  (`-')|   \\ |  | (`-')'.'  / |  .--./( OO).-.  ''`'-..__) |  .---'
         \\   /   / |  | |(OO ) |  |OO )|  . '|  |)(OO \\    / /_) (`-')( _) | |  ||  |  ' |(|  '--.
        _ \\     /_)|  | | |  \\(|  '__ ||  |\\    |  |  /   /) ||  |OO ) \\|  |)|  ||  |  / : |  .--'
        \\-'\\   /   \\  '-'(_ .' |     |'|  | \\   |  `-/   /` (_'  '--'\\  '  '-'  '|  '-'  / |  `---.
            `-'     `-----'    `-----' `--'  `--'    `--'      `-----'   `-----' `------'  `------'
                                                                    Copyright @pentest_swissky     """)
        print("\n{}Analyzing '{}' source code{}".format('' if results.plain else '\033[1m', results.dir, '' if results.plain else '\033[0m'))

        if os.path.isfile(results.dir):
            analysis(results.dirm, results.plain)
        else:
            recursive(results.dir, 0, results.plain)
        scanresults()

    else:
        parser.print_help()
