#!/usr/bin/python
import sys
#import re

# below script will extract keywords (line) from file1 
# search in file2
# if key not found append the commitId + keywords in result file (in append mode)

# open file2 as read mode
file2 = open('file2.txt', 'r') #second file 
readfile2 = file2.read()

# result file in overwrite mode
result = open('result.txt', 'w')

# iterate over file1
with open('file1.txt') as file1:
    for line in file1:
        
        #if re.search('Merge', line): # with re import
        #    continue 
        
        #if 'Merge' in line:     # with if condition
        #    continue

        words = line.split()
        commitId = "".join(words[0:1]) #extract commitId
        key = " ".join(words[1:]) #remove commitId from line
        # print (commit)

        # checking condition for key found or not in file2
        if key not in readfile2: 
            print(commitId + " " +key +"\n")
            result.write(commitId + " " +key +"\n")
        # else:  
        #     result.write(key +"\n")
        #     # print('String', key , 'Not Found')

# close all file objects
file1.close()
file2.close()
result.close()