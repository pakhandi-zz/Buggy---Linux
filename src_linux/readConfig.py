import json

def get(key):
	configs = json.loads(open('config').read())
	return configs[key]