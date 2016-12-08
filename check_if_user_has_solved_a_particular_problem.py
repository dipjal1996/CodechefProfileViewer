import requests
import sys
import urllib2
import re
import BeautifulSoup as BF

handle = raw_input(' Enter The Codechef Handle\n')
problemId = raw_input('Enter the problem code\n') 
url = 'https://www.codechef.com/users/' + handle

res = requests.get(url)

Bobject = BF.BeautifulSoup(res.text)
user_found = 0
for grab in Bobject.findAll('div'):
	if grab.get('class') == 'user-name-box' :
		user_found ^= 1
		break
if user_found == 0 : 
	print 'User not found!'
else :
	ok = 0
	for grab in Bobject.findAll('a') :
		if grab.text == problemId :
			ok ^= 1
			break
	if ok :
		print 'User ' + handle + ' has solved that problem!'
	else :
		print 'Invalid Problem Code or User ' + handle + ' has not solved that problem!'
