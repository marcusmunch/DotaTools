#!/usr/bin/env python

import dotatools

print("Current heroes in Dota 2 are:")
for i in dotatools.Hero._data:
	h = dotatools.Hero(i["id"])

	if h.localname:
		print("ID {:03d}: {:<25} 'Code' name: {}".format(i["id"], h.localname, h.name.title()))

print("\nHero data keys are: " + ', '.join(dotatools.Hero._data[0].keys()))