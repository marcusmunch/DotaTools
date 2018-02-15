#!/usr/bin/env python

import json

import requests
try:
	import requests_cache
	requests_cache.install_cache(expire_after=600)
except ImportError:
	pass

from .user import User
from .match import Match
from .hero import Hero
