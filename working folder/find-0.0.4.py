#!/usr/local/bin/python

import os
from optparse import OptionParser
from os.path import exists, join, walk, isfile, isdir
from os import listdir
import re
import csv
import time
import stat
import xml.etree.ElementTree as ET


def walkthru(path, writer):
    try:
        for d in os.listdir(path):
            if isdir(join(path,d)):
                if 'wp-includes' in d:
                    FileList = []
                    print ("Processing: " + join(path,d))
                    for file in os.listdir(path + '/' + d):
                        if isfile(os.path.join(path, os.path.join(d, file))):
                            if "version.php" in file and file.endswith("version.php"):
                                print("Version file found in " + path + '/' + d)
                                FileList.append(os.path.join(path, os.path.join(d, file)))
                    parser(FileList, writer)
                else:
                    walkthru(path + '/' + d, writer)
    except OSError as error:
        print (error)
        pass


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
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--path", action="store", type="string", dest="rootdir", help="specify the path")
    (options, args) = parser.parse_args()

    if options.rootdir is None:
        options.rootdir = raw_input('Enter a path to scan: ')

    timestr = time.strftime("%Y%m%d")
    # Create the csv file and add the header to the columns
    ofile = open('wp-version%s.csv' % timestr, 'w')
    print ("Output file created")
    writer = csv.writer(ofile, delimiter=' ')
    # writer.writerow(['Crawling results of %s' %options.rootdir])
    writer.writerow(['Path to wp instance', 'Version'])
    
    # Open the html output file
    tree = ET.parse('output.html')
    body = tree.getroot()
    child = Element("NewNode")
    body.append(child)
    tree.write('output.html')
    

    print ("Start to scan the files and subdirectories")
    walkthru(options.rootdir, writer)

    ofile.close()

    print ("Scan completed.")


if __name__ == "__main__":
    main()
