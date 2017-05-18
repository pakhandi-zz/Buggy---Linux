import os

def doWrite(filePath, content):
	fileObject = open(filePath, 'wb')
	fileObject.write(content)
	fileObject.close()

def createDir(dirPath):
	if (os.path.exists(dirPath)):
		print "Directory Exists: ", dirPath
	else:
		os.makedirs(dirPath)
