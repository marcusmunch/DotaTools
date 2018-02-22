#!/usr/bin/env python

import argparse

import dotatools

parser = argparse.ArgumentParser()
parser.add_argument('user_id', type=int)
args = parser.parse_args()

if args.user_id:
	u = dotatools.User(args.user_id)

	if not u.lastmatch:
		raise RuntimeError
		print("Found last match successfully!")
