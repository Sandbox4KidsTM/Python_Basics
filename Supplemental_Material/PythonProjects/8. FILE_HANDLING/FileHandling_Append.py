#appending to a textfile

#can append to an existing file or create a new file

fileVar = open("C:\\out\example3.txt", 'a') #'a' is for append handler
fileVar.write("pineapple")
fileVar.close()

#r: opens a file for reading only. 
#The file pointer is placed at the beginning of the file.
#This is the default mode

#r+: opens a file for both reading and writing. 
#The file pointer is placed at the beginning of the file.

#w: opens a file for writing only. 
#overwrites a file, if it exists.
#creates a file, if it does not exist.

#w+: opens a file for both reading and writing.
#overwrites a file, if it exists.
#creates a file, if it does not exist.

#a: opens a file for appending.
# the file pointer is at the end of the file, if the file exists.
# That is, the file is in the append mode.
# If the file does not exist, it creates a new file for writing.

#a+: opens a file for both appending and reading.
# the file pointer is at the end of the file, if the file exists.
# That is, the file is in the append mode.
# If the file does not exist, it creates a new file for writing.