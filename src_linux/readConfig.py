
def get(key):
	configFile = open('config', 'r')
	newDict = {}
	for line in configFile:
		listedline = line.strip().split(':',1)
		if len(listedline) > 1:
			newDict[listedline[0]] = listedline[1]
	val = newDict[key]

	val = val.lstrip(' ')
	val = val.rstrip(' ')

	return val