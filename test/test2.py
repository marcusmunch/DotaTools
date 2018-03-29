#!/usr/bin/env python

import sys

import dotatools

print("Current heroes in Dota 2 are:")

failcount = 0
id_lookup = 0

while failcount < 10:
    h = dotatools.Hero(id_lookup)

    if h.localname:
        if not "requests_cache" in sys.modules:
            print("ID {:03d}: {:<33} 'Code' name: {}".format(
                id_lookup, h.localname, h.codename.title()))
        else:
            pub_wr = '{:.2f}%'.format(h.stats["winrate"])
            print("ID {:03d}: {:<20}{} wins - 'Code' name: {}".format(id_lookup,
                                                                      h.localname, pub_wr, h.codename.title()))
    else:
        failcount += 1

    id_lookup += 1
