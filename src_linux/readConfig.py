
def getProxy():
	configFile = open('config', 'r')
	newDict = {}
	for line in configFile:
		listedline = line.strip().split(':',1)
		if len(listedline) > 1:
			newDict[listedline[0]] = listedline[1]
	proxyConfig = newDict["proxyConfig"]

	proxyConfig = proxyConfig.lstrip(' ')
	proxyConfig = proxyConfig.rstrip(' ')

	return proxyConfig