import requests
from bs4 import BeautifulSoup
import readConfig

import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def parseProblem(x, problemUrl, problemIndex):
	x = x.get(problemUrl)
	soup = BeautifulSoup(x.text)

	for divs in soup.findChildren('div', {"class": "part"}):
		for div in divs.findAll('section', {}):
			children = div.findChildren('h3')

			for child in children:
				headerString = div.h3.string
				# print "T"*5, "\n"
				if ("Input" in headerString) and ( ("Sample" in headerString) or ("Example" in headerString) ):
					print headerString
					inputCase = div.pre.string
					print inputCase
				if ("Output" in headerString) and ( ("Sample" in headerString) or ("Example" in headerString) ):
					print headerString
					outputCase = div.pre.string
					print outputCase

def test(xx, contestUrl = 'https://abc061.contest.atcoder.jp/assignments'):
	x = xx.get(contestUrl)
	soup = BeautifulSoup(x.text)
	num = 0
	for div in soup.findAll('tbody'):
		num += 1
		for row in div.findAll('tr'):
			cols = row.findAll('td')
			print ">",cols[0]
			ele = cols[0]
			ele = ele.findAll('a')
			problemRelativeUrl = ele[0]['href']
			problemUrl = 'https://abc061.contest.atcoder.jp' + problemRelativeUrl
			parseProblem(xx, problemUrl, num)

# Fill in your details here to be posted to the login form.
payload = {
	'name': readConfig.get("username"),
	'password': readConfig.get("password")
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
	p = s.post('https://practice.contest.atcoder.jp/login', data=payload)
	test(s)
