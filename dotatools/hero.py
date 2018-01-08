#!/usr/bin/env python

import requests, json

class Hero(object):
	try:
		r = requests.get("https://api.opendota.com/api/heroes", timeout=30)
	except requests.exceptions.ReadTimeout:
		print 'Request timed out!'
		exit(1)

	_data = json.loads(r.text)

	def __init__(self, hero_id):
		self.hero_id = hero_id

		for i in self._data:
			if i["id"] == hero_id:
				self.id = i["id"]


	@property
	def name(cls):
		try:
			return cls._data[cls.id]["name"][14:]
		except:
			pass

	@property
	def localname(cls):
		try:
			return cls._data[cls.id]["localized_name"]
		except:
			pass