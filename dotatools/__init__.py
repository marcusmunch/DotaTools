#!/usr/bin/env python

import json

import requests

class User(object):


	def __init__(self, steamID):
		self.steamID = steamID

		# Load profile data upon defining class object to reduce load on API
		r = requests.get('https://api.opendota.com/api/players/{}'.format(self.steamID))
		self._data = json.loads(r.text)

	@property
	def personaname(cls):
		"""Returns the 'personaname' or Steam nickname. This is only updated up until the most recent tracked match"""
		data = cls._data()

		return data["profile"]["personaname"].encode('utf-8')
