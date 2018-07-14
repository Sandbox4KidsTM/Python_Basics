
print("this is a file handling project")

fileObj = open("example1.txt",'r') #'r' stands for read, which is default mode
#once the file is open in Python, you cannot be deleted until it is closed

print(fileObj)
print(type(fileObj)) #this is of type: file object

contentOfFile = fileObj.read() #contents of the file are assigned to variable
print(contentOfFile)
print(type(contentOfFile)) #this is of type: str

fileObj.seek(0) #brings the pointer (or cursor) back to the top of the file
ContentLines = fileObj.readlines()
print(ContentLines)

fileObj.seek(0) 

contentLinesClean = [i.rstrip("\n") for i in ContentLines] #to strip out "\n" special character
print(contentLinesClean)
