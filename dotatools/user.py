import json

import requests

def getProfile(steamid):
	r = requests.get('https://api.opendota.com/api/players/%s' % steamid)
	return json.loads(r.text)