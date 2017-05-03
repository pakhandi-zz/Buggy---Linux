import os
from bs4 import BeautifulSoup
import sys
import shutil
import urllib2
import readConfig

CFRound = sys.argv[1]

url = "http://codeforces.com/contest/"+CFRound+"/problems"

try:
	print "Trying direct connection"
	proxy = urllib2.ProxyHandler({})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)
	response = urllib2.urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data)
except Exception:
	try:
		print "Direct Connection Failed, trying Proxy"

		proxyConfig = readConfig.get("proxyConfig")

		if len(proxyConfig) != 0:
			proxy = urllib2.ProxyHandler({'http' : proxyConfig })
			opener = urllib2.build_opener(proxy)
			urllib2.install_opener(opener)

		response = urllib2.urlopen(url)
		data = response.read()
		soup = BeautifulSoup(data)
	except Exception:
		print "Error in Connection to Internet"

present=1

for x in soup.findAll('li', 'current'):
	present=0

if present == 0:
	sys.exit()

customPath = os.path.expanduser(readConfig.get("path"))
		
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
	
	if (os.path.exists(customPath + CFRound + "/" + chr(ord('A') + counter))):
		print "Folder Exists"
	else:
		os.makedirs(customPath + CFRound + "/" + chr(ord('A') + counter))

	shutil.copyfile("temp",customPath + CFRound + "/" + chr(ord('A') + counter) + "/round")
	shutil.copyfile("template.cpp", customPath + CFRound + "/" + chr(ord('A') + counter) + "/aprog.cpp" )
	shutil.copyfile("template.java", customPath + CFRound + "/" + chr(ord('A') + counter) + "/aprog.java" )

	
	detach_dir = customPath + CFRound + "/" + chr(ord('A') + counter) + "/"
	att_path = os.path.join(detach_dir, chr(ord('A')+counter)+".cpp")
	counter+=1
	incounter = 1

	div = div.find('div', 'sample-tests')

	for item in div.findAll('pre'):
		if incounter%2 == 1:
			fileName = readConfig.get("inputFileFormat")
			fileName = fileName.replace("$number$", str(incounter / 2))
			att_path = os.path.join(detach_dir, fileName)
			print att_path
			f = open(att_path, 'wb')
		else:
			fileName = readConfig.get("outputFileFormat")
			fileName = fileName.replace("$number$", str((incounter / 2) - 1))
			att_path = os.path.join(detach_dir, fileName)
			print att_path
			f = open(att_path, 'wb')
		incounter+=1
		item = str(item).replace("<pre>", "")
		item = str(item).replace("</pre>", "")
		item = str(item).replace("<br/>", "\n")
		f.write(item)

detach_dir = "."
att_path = os.path.join(detach_dir, "temp")
f = open(att_path, 'wb')
f.write(customPath)
f.close()