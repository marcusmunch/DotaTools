#!/usr/bin/env python

class User(object):

	def __init__(self, steamID):
		import requests, json
		self.steamID = steamID

		# Load profile data upon defining class object to reduce load on API
		r = requests.get('https://api.opendota.com/api/players/{}'.format(self.steamID))
		self._data = json.loads(r.text)

	@property
	def personaname(self):
		"""Returns the 'personaname' or Steam nickname. This is only updated up until the most recent tracked match"""
		data = self._data

		return data["profile"]["personaname"].encode('utf-8')
