#!/usr/bin/env python

import requests, json, re, sys, time

def build_database():
	try:
		r = requests.get("https://api.opendota.com/api/heroes", timeout=10)
	except requests.exceptions.ReadTimeout:
		print("Request timed out!")
		exit(1)

	data = json.loads(r.text)
	heroes = {}
	for h in data:
		heroes.update({h["id"]: h})

	return heroes


class Hero(object):
	database = build_database()

	def __init__(self, hero_id):
		self.heroes = self.database
		self.hero_id = hero_id

	@property
	def data(cls):
		try:
			return cls.heroes[cls.hero_id]
		except:
			return None

	@property
	def codename(cls):
		if cls.data: return cls.data["name"]

	@property
	def localname(cls):
		if cls.data: return cls.data["localized_name"]

	@property
	def stats(cls):
		if not cls.data: return None

		try:
			if not "requests_cache" in sys.modules:
				time.sleep(0.5)
			r = requests.get("https://api.opendota.com/api/heroStats", timeout=30)
			herostats = json.loads(r.text)

		except requests.exceptions.ReadTimeout:
			print("Request timed out!")
			exit(1)

		for hero in herostats:
			picks = 0
			wins = 0
			for stat in hero:
				if re.search('^\d+_pick', stat):
					picks += int(hero[stat])
				if re.search('^\d+_win', stat):
					wins += int(hero[stat])
			winrate = wins*100.0 / picks
			hero.update({"picks": picks})
			hero.update({"wins": wins})
			hero.update({"winrate": winrate})

		for h in herostats:
			if h["id"] == cls.hero_id:
				return h
