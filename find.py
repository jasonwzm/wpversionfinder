#!/usr/local/bin/python

import os
#import argparse			# from argparse import ArgumentParser
from optparse import OptionParser
from os.path import exists, join
import re
import csv
import time
import stat

# Helper for the options
usage = "usage: %prog [options] arg1 arg2"
#parser = argparse.ArgumentParser()
parser = OptionParser(usage = usage)
parser.add_option("-p", "--path", action="store", type="string", dest="rootdir", help="specify the path")
#parser.add_argument("-p", "--path", action="store", type=str, #dest="rootdir", help="specify the path")
#parser.add_argument("-s", "--subdirectory", action="store", type=str, dest="subdir", help="specify the directory")

#parser.parse_args()
#args = parser.parse_args()
(options, args) = parser.parse_args()

timestr = time.strftime("%Y%m%d")    
# Create the csv file and add the header to the columns
ofile = open('wp-version%s.csv' %timestr, 'w')
writer = csv.writer(ofile, delimiter=' ')
#writer.writerow(['Crawling results of %s' %options.rootdir])
writer.writerow(['Path Name', 'Version'])


FileList = []
#print args:  
#for root, dirs, files in os.walk(args.path): 
for root, dirs, files in os.walk(options.rootdir):    
#print root
    # Search for files with certain names included  
	#for s in root:  
        #if s.find(args.subdir) != -1:  
	#print dirs
	#for r in root:
#	stat.S_ISDIR(os.stat(args.path).st_mode)
#	print oct(stat.S_ISDIR(os.stat(args.path).st_mode)

    for d in files:
            FileList.append(os.path.join(root, d))
#print FileList

#print ("%s", FileList)

for item in FileList:  
	#print item[11:]
	if "version.php" in item:
	#if item[11:]=="version.php":	
#		print 'it worked'
    # Get the path name for the location of wp-config file
    #path_name = item[:item.rindex('/')] + "/wp-includes/"
    #if exists(join(path_name, 'version.php')):
        # Find the README file that exists in the same folder for wp-config file
        	with open(item) as inF:
        	    for line in inF:
        	        # Find the line with Version information
        	        if '$wp_version =' in line:
        	            # Line parser
        	            sent_split = line.split('\'')[1]
        	            version = sent_split
        	            item = ''.join(item.split())
        	            version1 = ''.join(version.split())
        	            data = [item, version1]
        	            # Write data into the csv file
        	            writer.writerow(data)
	#else:
		#print ("file does not exist!")
ofile.close()

