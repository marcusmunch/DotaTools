#!/usr/bin/env python

try:
    import requests_cache

    requests_cache.install_cache(expire_after=600)
except ImportError:
    requests_cache = None
    pass

from .hero import Hero
from .match import Match
from .user import User
