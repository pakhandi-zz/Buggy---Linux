import os
from bs4 import BeautifulSoup
import sys
import shutil
import urllib2

#print "Enter the round number : "
CF = int(sys.argv[1])

url = "http://codeforces.com/contest/"+CF+"/problems"

try:
	print "Trying direct connection"
	response = urllib2.urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data)
except Exception, e:
	print "Direct Connection Failed, trying Proxy"
	proxy_file = open("proxy.txt", 'r')

	newDict = {}
	for line in proxy_file:
		# print line
		listedline = line.strip().split(':')

		if len(listedline) > 1:
			newDict[listedline[0]] = listedline[1]

	proxy_config = newDict["proxy_config"]

	if len(proxy_config) != 0:
		proxy = urllib2.ProxyHandler({'http'    : proxy_config})
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)

	response = urllib2.urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data)
finally:
	print "Error in Connection to Internet"

#soup = BeautifulSoup(data.text)

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
			att_path = os.path.join(detach_dir, "in"+str(incounter/2)+".txt")
			print att_path
			f = open(att_path, 'wb')
		else:
			att_path = os.path.join(detach_dir, "out"+str((incounter/2)-1)+".txt")
			print att_path
			f = open(att_path, 'wb')
		incounter+=1
		item = str(item).replace("<pre>", "")
		item = str(item).replace("</pre>", "")
		item = str(item).replace("<br/>", "\n")
		f.write(item)

#shutil.copyfile("f.bat", "340/C/f.bat")
