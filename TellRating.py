import requests
import sys
import urllib2
import re
import BeautifulSoup

handle = raw_input(' Enter The Codechef Handle') # or take from terminal

url = 'https://www.codechef.com/users/' + handle

res = requests.get(url)

Bobject = BeautifulSoup.BeautifulSoup(res.text)

for grab in Bobject.findAll('div'):# , class = 'user-name-box'):
	if grab.get('class') == 'user-name-box' :
		print 'Name is ' + grab.text
		break
 
 #CURRENT RATINGS  LONG
f = 1
for grab in Bobject.findAll('a' , href = re.compile('^http://www.codechef.com/ratings/long-challenge?')):
	if( f % 2 != 0):
 		print 'Long Contest (Global) ' + grab.text
 		f += 1
 	else:
 		print 'Long Contest (Local) ' + grab.text
 #CURRENT RATINGS  SHORT
f = 1
for grab in Bobject.findAll('a' , href = re.compile('^http://www.codechef.com/ratings/cook-off')):
	if( f % 2 != 0):
 		print 'Short (Global) ' + grab.text
 		f += 1
 	else:
 		print 'Short (Local) ' + grab.text
 #CURRENT RATINGS  LTime
f = 1
for grab in Bobject.findAll('a' , href = re.compile('^http://www.codechef.com/ratings/lunch-time')):
	if( f % 2 != 0):
 		print 'Ltime (Global) ' + grab.text
 		f += 1
 	else:
 		print 'Ltime (Local) ' + grab.text
