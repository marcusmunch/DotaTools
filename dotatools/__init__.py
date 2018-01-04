from . import user

def profile(steamID):
	return user.getProfile(steamID)