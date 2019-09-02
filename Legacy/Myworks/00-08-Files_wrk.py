import os

#Working Directory
print ('\nWorking Directory\n', os.getcwd())

#create file only if not exists
#f1 =open('file.txt','x')

# create file
f1 = open('file.txt','a')
f1.write('\n\nHello line2')



#overwrite the content

#f1 = open('file.txt','w')

f1.write('\noverwrite data')



#delete file

f1 =os.remove('file.txt')


#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#
#"x" - Create - Creates the specified file, returns an error if the file exists


#Open test file

f= open('test.txt')

#over write data

f = open('test.txt','w')

f.write('Start this is line1\nLine2\nEnd of Line3')

# read comments from files

f = open('test.txt','r')

print('\n----PRINT FILE CONTENT---\n',f.read())

#seek value to 0

f.seek(0)

# print characters
print('\n-----PRINT 1st 5 characters---\n',f.read(5))


# read lines readline()
f.seek(0)

f = open('test.txt','r')

print('\n--ReadLine 1--\n', f.readline())

f.seek(0)
print ('\n--- Read multiple lines --\n', f.readline())
print(f.readline())

#### print all lines
f.seek(0)
print ('--------Read all lines with readlines()----')
print (f.readlines())

#loop through the file line by line

f = open('test.txt','r')

print('\n--------Loop started-')
for x in f:
    print(x)


#Check if file exist

print(os.getcwd())

if os.path.exists('test.txt'):
    print('File exists')
else:
    print('File does not exists')

#print all files in directory
dir = os.getcwd()

print ('\n--------List Directories--\n' , os.listdir(dir))

file_list = os.listdir()

#Print all files in directory list

print ('\n------Files in directory list------\n')
i = 0
for file in file_list:
    i = i +1
    print(i,'\t', file)

f.seek(0)

print (f.read())

f.seek(0)

print (f.readline())

f.seek(0)
print(f.readlines())

f.seek(0)
for line in f.readlines():
    print(line)


import csv
import gzip
import bz2
import zipfile
from zipfile import ZipFile

with ZipFile('/Users/mbheri/Downloads/files.zip') as files:
    print(files.namelist())
    print(files.extractall())



