# coding:utf-8
import urllib 
import time
import zipfile  
import os  
def pojie_zip(zip_path,password):  
    if zip_path[-4:]=='.zip':  
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
def get_pass(zip_path,date):
	print 'Try the password %s' % date[-4:]
	if pojie_zip(zip_path,date[-4:]):
		return True
	pass_path='zip.txt'
	passFile=open(pass_path,'r')
	for line in passFile.readlines():
		password=line.strip('\n')
		print 'Try the password %s' % password
		if pojie_zip(zip_path,password):
			return True
def get_zip(zip_path,sys_hosts_path,date):
	url = 'https://iiio.io/download/'+str(date)+'/Windows系列跟苹果系列.zip'
	content=urllib.urlopen(url)
	if content.getcode()==200:
		urllib.urlretrieve(url, zip_path)
		print str(date)+'  get zip done'
		get_pass(zip_path,date)
		# if get_pass(zip_path):
			# change_hosts(sys_hosts_path)
	else:
		new_date = int(date)-1
		print str(date)+' Nothing'
		get_zip(zip_path,sys_hosts_path,str(new_date))
		# time.sleep(1000)  
def change_hosts(sys_hosts_path):
	os.remove(sys_hosts_path)
	shutil.move("hosts",sys_hosts_path)
if __name__=='__main__':
	sys_hosts_path='C:\\Windows\\System32\\drivers\\etc\\hosts'
	zip_path = r'hosts.zip' 
	date =  time.strftime('%Y%m%d',time.localtime(time.time())) 
	get_zip(zip_path,sys_hosts_path,str(date))  
