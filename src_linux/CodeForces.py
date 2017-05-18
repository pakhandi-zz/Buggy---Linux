import requests
from bs4 import BeautifulSoup
import sys
import os
import readConfig
import FileHelper

def parseContest(sessionElement, contestId):
	contestUrl = getContestUrl(contestId)
	allProblemsPage = sessionElement.get(contestUrl)
	allProblemsPageText = BeautifulSoup(allProblemsPage.text)
	problemIndex = 0

	for div in allProblemsPageText.findAll('div', 'problemindexholder'):
		for innerDiv in div.findAll('div', 'sample-tests'):

			basePath = os.path.expanduser(readConfig.get("CodeForcesPath"))
			contestPath = os.path.join(basePath, contestId)

			problemPath = os.path.join(contestPath, chr(ord('A') + problemIndex))
			FileHelper.createDir(problemPath)

			FileHelper.copyFile("template.cpp", os.path.join(problemPath, "sol.cpp"))
			FileHelper.copyFile("template.java", os.path.join(problemPath, "sol.java"))

			inputCaseNumber = 0
			outputCaseNumber = 0

			caseNumber = 0
			for preTag in innerDiv.findAll('pre'):
				for br in preTag.findAll('br'):
					br.replace_with('\n')
				if caseNumber % 2 == 0:
					inputCase = preTag.text
					testFileName = readConfig.get("inputFileFormat")
					testFileName = testFileName.replace("$testCaseNumber$", str(inputCaseNumber))
					testFile = os.path.join(problemPath, testFileName)
					FileHelper.doWrite(testFile, inputCase)
					inputCaseNumber += 1
				else:
					outputCase = preTag.text
					testFileName = readConfig.get("outputFileFormat")
					testFileName = testFileName.replace("$testCaseNumber$", str(outputCaseNumber))
					testFile = os.path.join(problemPath, testFileName)
					FileHelper.doWrite(testFile, outputCase)
					outputCaseNumber += 1
				caseNumber += 1
		problemIndex += 1

def getContestUrl(contestId):
	return "http://codeforces.com/contest/" + contestId + "/problems"

def doParsing(contestId):
	payload = {}
	
	with requests.Session() as sessionElement:
		parseContest(sessionElement, contestId)

# call it
contestId = sys.argv[1]
doParsing(contestId)