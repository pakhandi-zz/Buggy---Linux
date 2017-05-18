import requests
from bs4 import BeautifulSoup
import readConfig
import sys
import os
import FileHelper

def parseProblem(sessionElement, contestId, problemRelativeUrl, problemIndex):
	problemUrl = getProblemUrl(contestId, problemRelativeUrl)
	problemPage = sessionElement.get(problemUrl)
	problemPageText = BeautifulSoup(problemPage.text)

	print "#"*20, problemIndex, "$"*20

	basePath = os.path.expanduser(readConfig.get("path"))
	# contestPath = contestId
	contestPath = os.path.join(basePath, contestId)

	problemPath = os.path.join(contestPath, chr(ord('A') + problemIndex))
	FileHelper.createDir(problemPath)

	inputCaseNumber = 0
	outputCaseNumber = 0

	for divs in problemPageText.findChildren('div', {"class": "part"}):
		for div in divs.findAll('section', {}):
			children = div.findChildren('h3')
			for child in children:
				headerString = div.h3.string
				if ("Input" in headerString) and ( ("Sample" in headerString) or ("Example" in headerString) ):
					inputCase = div.pre.string
					print "Case: ", inputCaseNumber
					print inputCase
					testFileName = readConfig.get("inputFileFormat")
					testFileName = testFileName.replace("$testCaseNumber$", str(inputCaseNumber))
					testFile = os.path.join(problemPath, testFileName)
					FileHelper.doWrite(testFile, inputCase)
					inputCaseNumber += 1
				if ("Output" in headerString) and ( ("Sample" in headerString) or ("Example" in headerString) ):
					outputCase = div.pre.string
					print "Case: ", outputCaseNumber
					print outputCase
					testFileName = readConfig.get("outputFileFormat")
					testFileName = testFileName.replace("$testCaseNumber$", str(outputCaseNumber))
					testFile = os.path.join(problemPath, testFileName)
					FileHelper.doWrite(testFile, outputCase)
					outputCaseNumber += 1

def parseContest(sessionElement, contestId):
	contestUrl = getAllProblemsUrl(contestId)
	print contestUrl
	allProblemsPage = sessionElement.get(contestUrl)
	allProblemsPageText = BeautifulSoup(allProblemsPage.text)
	num = 0
	for div in allProblemsPageText.findAll('tbody'):
		for row in div.findAll('tr'):
			cols = row.findAll('td')
			problemTag = cols[0]
			problemLinkTag = problemTag.findAll('a')
			problemRelativeUrl = problemLinkTag[0]['href']
			# problemUrl = getProblemUrl(contestId, problemRelativeUrl)
			parseProblem(sessionElement, contestId, problemRelativeUrl, num)
			num += 1

def getContestUrl(contestId):
	return "https://" + contestId + ".contest.atcoder.jp/"

def getAllProblemsUrl(contestId):
	contestUrl = getContestUrl(contestId)
	return contestUrl + "assignments/"

def getProblemUrl(contestId, problemRelativeUrl):
	contestUrl = getContestUrl(contestId)
	return contestUrl + problemRelativeUrl

def getLoginUrl(contestId):
	contestUrl = getContestUrl(contestId)
	return contestUrl + "login/"

def doParsing(contestId):
	payload = {
		'name': readConfig.get("username"),
		'password': readConfig.get("password")
	}
	
	with requests.Session() as sessionElement:
		retVal = sessionElement.post(getLoginUrl(contestId), data=payload)
		parseContest(sessionElement, contestId)

# call it
contestId = sys.argv[1]
doParsing(contestId)