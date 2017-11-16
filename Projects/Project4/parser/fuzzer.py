#!/usr/bin/python
import subprocess
import os
import base64
import sys
import json
import string
import random

def id_generator(size=3, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

find=0;
def test(testcase):
	child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	_, stdErrOut = child.communicate(input = testcase);
	#print testcase
	if child.returncode == -11: # or stdErrOut != "" :
		#print "BROKEN SUCCESS TEST CASE (%d): %s" % (child.returncode, testcase)
		#print "|%s|" % stdErrOut
		#print -11
		find=1
		sys.exit(0)
		print base64.b64encode(testcase)

n=30
while find==0:
	s='{\"'+id_generator() +'\":{'
	for i in range(0,10000*n):
		s0=id_generator()
		s+='\"'+s0 +'\":{'
	s+='\"a\":1'
	for i in range(0,10000*n+2):
		s+='}'
	#print s
	test(s)
	n+=1

