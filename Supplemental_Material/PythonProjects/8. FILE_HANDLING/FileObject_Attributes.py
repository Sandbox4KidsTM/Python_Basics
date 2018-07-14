#file object attributes

fileObj = open("C:\\in\\example.txt", 'r')
fileContent = fileObj.read()
print("Name of the file:" , fileObj.name)
print("File is closed or not: ", fileObj.closed)
print("Opening mode: ", fileObj.mode)