#!/usr/local/bin/python

import os
#import argparse                        # from argparse import ArgumentParser
from optparse import OptionParser
from os.path import exists, join
import re
import csv
import time
import stat

# Helper for the options
usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage = usage)
parser.add_option("-p", "--path", action="store", type="string", dest="rootdir", help="specify the path")
(options, args) = parser.parse_args()

timestr = time.strftime("%Y%m%d")    
# Create the csv file and add the header to the columns
ofile = open('wp-version%s.csv' %timestr, 'w')
writer = csv.writer(ofile, delimiter=' ')
#writer.writerow(['Crawling results of %s' %options.rootdir])
writer.writerow(['Path Name', 'Version'])


FileList = []
for root, dirs, files in os.walk(options.rootdir): 

    for d in dirs:
        if 'wp' in os.path.dirname(d):
            for files in os.walk(d):
                for f in files:
                    FileList.append(os.path.join(root, f))
               
for item in FileList:  
        if "version.php" in item:
                with open(item) as inF:
                    for line in inF:
                        # Find the line with Version information
                        if '$wp_version =' in line:
                            # Line parser
                            sent_split = line.split('\'')[1]
                            version = sent_split
                            item = ''.join(item.split())
                            version1 = ''.join(version.split())
                            iteminParts = item.split('/');
                            data = [iteminParts[3], version1]
                            # Write data into the csv file
                            writer.writerow(data)
        #else:
                #print ("file does not exist!")
ofile.close()
