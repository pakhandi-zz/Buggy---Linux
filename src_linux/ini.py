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
	print "Direct Connection Failed, trying Proxy"

	proxyConfig = readConfig.getProxy()

	print proxyConfig

	if len(proxyConfig) != 0:
		proxy = urllib2.ProxyHandler({'http' : proxyConfig })
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)

	response = urllib2.urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data)
else:
	print "Error in Connection to Internet"

present=1

for x in soup.findAll('li', 'current'):
	present=0

if present == 0:
	sys.exit()
		
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
	
	if (os.path.exists(CFRound+"/"+chr(ord('A')+counter))):
		print "Folder Exists"
	else:
		os.makedirs(CFRound+"/"+chr(ord('A')+counter))

	shutil.copyfile("temp.txt",CFRound+"/"+chr(ord('A')+counter)+"/round")
	shutil.copyfile("template.cpp", CFRound+"/"+chr(ord('A')+counter)+"/aprog.cpp" )
	
	detach_dir = CFRound+"/"+chr(ord('A')+counter)+"/"
	att_path = os.path.join(detach_dir, chr(ord('A')+counter)+".cpp")
	counter+=1
	incounter = 1
	for item in div.findAll('pre'):
		if incounter%2 == 1:
			att_path = os.path.join(detach_dir, "in"+str(incounter/2))
			print att_path
			f = open(att_path, 'wb')
		else:
			att_path = os.path.join(detach_dir, "out"+str((incounter/2)-1))
			print att_path
			f = open(att_path, 'wb')
		incounter+=1
		item = str(item).replace("<pre>", "")
		item = str(item).replace("</pre>", "")
		item = str(item).replace("<br/>", "\n")
		f.write(item)