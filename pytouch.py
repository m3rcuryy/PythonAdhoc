#!/usr/bin/python2

import  sys
import re
import os
file_name=sys.argv[1:]


for  i  in  file_name:
	if i[-1]=="}" and i[-3]=="." and i[-4]=="." and a[-2].isdigit() and a[-5].isdidgit() and a[-6]=="{":
		tem=i[0:-6]
		for k in range(min(int(i[-5]),int(-2)),max((int(i[-5]),int(-2)))):
			if not(os.path.isfile(tem+str(k)) or os.path.isdir(tem+str(k))): 
				os.mkdir(tem+str(k))
		pass
	if not(os.path.isfile(i) or os.path.isdir(i)):
		os.mkdir(i)
	
