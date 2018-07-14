# open and read file

FileObj = open("DataFile.txt")
print(type(FileObj))

FileContent = FileObj.read()
print(FileContent)

FileObj.seek(0)
FileContent2 = FileObj.readlines()
print(FileContent2)

