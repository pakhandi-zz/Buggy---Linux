import os
import shutil

def doWrite(filePath, content):
	print "Creating file: ", filePath
	fileObject = open(filePath, 'wb')
	fileObject.write(content)
	fileObject.close()

def createDir(dirPath):
	print "Creating directory: ", dirPath
	if (os.path.exists(dirPath)):
		print "Directory Exists: ", dirPath
	else:
		os.makedirs(dirPath)

def copyFile(sourceFile, targetFile):
	print "Copying: ", sourceFile, " -> ", targetFile
	shutil.copyfile(sourceFile, targetFile)