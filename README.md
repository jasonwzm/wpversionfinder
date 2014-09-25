wpversionfinder
===============


About this document

If you would like to get the most recent copy of the WebApp Finder tool and run it, you are looking at the right document

Getting the tool

Find the code here: https://github.com/jasonwzm/wpversionfinder

Prerequisites

You need a host with python 2.6 to use this tool

Background on the tool

The application is used to find out the versions of the wordpress that different user accounts host. Detailed requirement and ideas can be found at here. This document serves as the documentation of the development and the application of different versions.

Version-specific notes

Version 0.1 (Tested in May 2014)
    The first version of the application (written in Python) provides a prototype of the functions of the application. It uses the idea to find the wp-config file in the public/html or public/vhost directories. The application offers a more generic option--search in a specified path for a specified file. Users are required to type in the command to run the script and two options are required (-p for PATH and -f for FILENAME). In addition, the application generates a .csv file that contains the version of wordpress and send the file to the hardcoded email address. 

Here is how the usage is defined:    
    usage = "usage: %prog [options] arg1 arg2"
    
    .csv file is created to include the version and file information:
    ofile = open('wp-version%s.csv' %timestr, 'w')

    Search for files with certain names included
    for f in files:  
        if f.find(options.filename) != -1:  
            FileList.append(os.path.join(root, f))

    Find the README file that exists in the same folder for wp-config file
    with open("README.html") as inF:

    Find the line with Version information
    if '<br /> Version' in line:

    The program will parse the line and the return the version number.
    The information will be put into the csv file.

    It will include the csv file as an attachment to the email.
    The sender is a TEST-ONLY email account.

    The follow message will be shown on screen if the email is correctly sent
    email sent

Version 0.2 (Modified by Ashlee from Version 0.1)
    The version removes the function that sends an email after the search is completed.
    The program looks for version.php file in the directory.
    It will return all the version numbers found.
    Improvements from the previous are that:
Doing complete recursive calls
Give feedback to the current user on the process of the program
Improve the performance of the application by restricting the look up to only wp-includes folder
Improve user feedback by continuously output, instead of outputting at the end.

Version 1.0 
    The idea behind this version is to focus on the version lookup, checking and validation of the wordpress pages. Techniques include searching for folder and parsing the html page of the blog.
