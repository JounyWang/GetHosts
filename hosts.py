#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By linjie
# Python 2.7
import urllib2
import os
from bs4 import BeautifulSoup
import urllib 
import time
import zipfile  
import os  
def pojie_zip(zip_path,password):  
    zip = zipfile.ZipFile(zip_path, "r",zipfile.zlib.DEFLATED)  
    try:
        zip.extractall(members=zip.namelist() , pwd=password)  
        print ' ----success!,The password is %s' % password  
        zip.close()
        os.remove(zip_path)  
        return True  
    except:  
        pass
    print 'error'
def get_zip(zip_path,date,pwd):
	url = 'https://iiio.io/download/'+str(date)+'/Windows系列跟苹果系列.zip'
	content=urllib.urlopen(url)
	if content.getcode()==200:
		urllib.urlretrieve(url, zip_path)
		print str(date)+'  get zip done'
		pojie_zip(zip_path,pwd)
	else:
		print str(date)+' Nothing'
		get_zip(zip_path,str(int(date)-1),pwd)
def get_pwd(url):
	tags = BeautifulSoup(urllib2.urlopen(url).read(),"lxml").find_all('span',style="color: #3366ff;")
	for tag in tags:
		return tag.string.split('密码：'.decode('utf-8'))[1]
if __name__=='__main__':
	url='https://laod.cn/hosts/2017-google-hosts.html'
	pwd = get_pwd(url)
	zip_path = r'hosts.zip' 
	date =  time.strftime('%Y%m%d',time.localtime(time.time())) 
	get_zip(zip_path,str(date),pwd)
	os.system('hosts.bat')   
