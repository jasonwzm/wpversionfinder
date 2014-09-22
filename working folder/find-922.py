#!/usr/local/bin/python

import os
from optparse import OptionParser
from os.path import exists, join, walk
import re
import csv
import time
import stat

def walkthru(path, writer):
  for root, dirs, files in os.walk(path): 
    for d in dirs:
      if 'wp-includes' in d:
	FileList = []
	print ("Processing: "+path+"/"+d)
	for rootdirs, directories, filenames in os.walk(path+"/"+d):
	  for file in filenames:
	  	if "version.php" in file:
		  print("Version file found in "+path+"/"+d)
		  FileList.append(os.path.join(root, os.path.join(d, file)))
		  parser(FileList, writer)
      else:
	walkthru(path+"/"+d, writer)

def parser(FileList, writer):
  for item in FileList: 
      with open(item) as inF:
	  for line in inF:
	      # Find the line with Version information
	      if '$wp_version =' in line:
		  lastIndex = item.rindex('/')
		  item = item[:lastIndex]
		  # Line parser
		  sent_split = line.split('\'')[1]
		  version = sent_split
		  version1 = ''.join(version.split())
		  data = [item, version1]
		  # Write data into the csv file
		  writer.writerow(data)  


def main():

  # Helper for the options
  usage = "usage: %prog [options] arg1 arg2"
  parser = OptionParser(usage = usage)
  parser.add_option("-p", "--path", action="store", type="string", dest="rootdir", help="specify the path")
  (options, args) = parser.parse_args()
    
  if options.rootdir is None:
    options.rootdir = raw_input('Enter a path to scan: ')
  
  timestr = time.strftime("%Y%m%d")    
  # Create the csv file and add the header to the columns
  ofile = open('wp-version%s.csv' %timestr, 'w')
  print ("Output file created")
  writer = csv.writer(ofile, delimiter=' ')
  #writer.writerow(['Crawling results of %s' %options.rootdir])
  writer.writerow(['Path to wp instance', 'Version'])

  print ("Start to scan the files and subdirectories")
  walkthru(options.rootdir, writer)
	 		  
  ofile.close()
  
  print ("Scan completed.")


if __name__ == "__main__":
  main()
