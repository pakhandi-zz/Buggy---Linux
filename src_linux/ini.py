import os
from bs4 import BeautifulSoup
import sys
import shutil
import urllib2

CF = int(sys.argv[1])

url = "http://codeforces.com/contest/"+CF+"/problems"

try:
	print "Trying direct connection"
	response = urllib2.urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data)
except Exception, e:
	print "Direct Connection Failed, trying Proxy"
	
	configFile = open('config', 'r')
	newDict = {}
	for line in configFile:
		listedline = line.strip().split(':')
		if len(listedline) > 1:
			newDict[listedline[0]] = listedline[1]
	proxyConfig = newDict["proxy_config"]

	if len(proxyConfig) != 0:
		proxy = urllib2.ProxyHandler({'http' : proxy_config})
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)

	response = urllib2.urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data)
finally:
	print "Error in Connection to Internet"

present=1

for x in soup.findAll('li', 'current'):
	present=0
	print x.text

if present == 0:
	exit()
		
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
	
	if (os.path.exists(CF+"/"+chr(ord('A')+counter))):
		print "Folder Exists"
	else:
		os.makedirs(CF+"/"+chr(ord('A')+counter))

	shutil.copyfile("temp.txt",CF+"/"+chr(ord('A')+counter)+"/round.txt")
	shutil.copyfile("template.cpp", CF+"/"+chr(ord('A')+counter)+"/aprog.cpp" )
	
	detach_dir = CF+"/"+chr(ord('A')+counter)+"/"
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