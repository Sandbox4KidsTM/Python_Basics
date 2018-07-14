#file positions

fileObj = open("C:\\in\\example.txt", 'r')
fileCont = fileObj.read() #without parameter, read will read the entire file
print(fileCont)

print("------") #empty string as a separator

fileObj.seek(0, 1) #sets the pointer to the specified position 
# seek(offet[, from]), where offset argument indicates the number of bytes to be moved
# from argument specifies the reference position from where the bypes are to be moved
# from argument can be 0(beginning of file), 1(current position of file), or 2 (end of file)
print(fileObj.tell()) #tells the position of the current cursor/pointer in the file

fileObj.seek(0, 0)
fileCont = fileObj.read(15) #with parameter, read will read the next 10 characters of the file from current position
#newline characters are also counted in the read
print(fileCont)

fileObj.close()