import requests
import os
from bs4 import BeautifulSoup
import shutil

#print "Enter the round number : "
CF = raw_input()

url = "http://codeforces.com/contest/"+CF+"/problems"

lag=0
try:
    data = requests.get(url)
    flag = 1
except Exception, e:
    print "Direct Connection Failed, trying Proxy"
    fo = open("proxy.txt", "r+")
    http_proxy = fo.read(100)
    fo.close()

    proxyDict = { 
                   "http"  : "http://"+http_proxy
                }

    data = requests.get(url, proxies=proxyDict)
    flag=1

if flag==0:
    print "Error in Connection to Internet"

data = requests.get(url)

soup = BeautifulSoup(data.text)

present=1

for x in soup.findAll('li', 'current'):
    present=0
    print x.text

if present == 0:
    exit()

'''
for div in soup.findAll('div', 'problemindexholder'):
    count = 0
    for item in div.findAll('div'):
        count+=1
        if count == 13:
            print "\n\n\nPROBLEM STATEMENT : "
            print item.text
        if count == 14:
            print "\n\n\nINPUT : "
            print item.text
        if count == 16:
            print "\n\n\nOUTPUT : "
            print item.text
'''
        
counter = 0
for div in soup.findAll('div', 'problemindexholder'):
    
    if (os.path.exists(CF+"/"+chr(ord('A')+counter))):
        print "Folder Exists"
    else:
        os.makedirs(CF+"/"+chr(ord('A')+counter))

    shutil.copyfile("zz.sh",CF+"/"+chr(ord('A')+counter)+"/zz.sh")
    shutil.copyfile("zy.sh",CF+"/"+chr(ord('A')+counter)+"/zy.sh")
    shutil.copyfile("zx.sh",CF+"/"+chr(ord('A')+counter)+"/zx.sh")
    shutil.copyfile("temp.txt",CF+"/"+chr(ord('A')+counter)+"/round.txt")
    shutil.copyfile("template.cpp", CF+"/"+chr(ord('A')+counter)+"/prog.cpp" )
    
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
