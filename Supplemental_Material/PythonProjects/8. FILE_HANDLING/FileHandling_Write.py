# this program creates and writes to a file

fileVar = open("C:\\out\\example_write.txt", 'w') #(creates an empty file and) opens a file in write mode
fileVar.write("Line1") #wites content to the file
fileVar.write("Line2\n")
fileVar.write("Line3\n")
fileVar.write("Line4\n")
fileVar.close() #closes the file, so the file and its contents may be accessed by another program
#print(fileVar.read()) #ValueError: I/O operation on closed file.
#close method saves the contents to the file 

fileVar = open("C:\\out\\example_write.txt", 'r')
print(fileVar.read()) #print the contents of the fileVar
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'w') #overwrites old content
fileVar.write("Line5\n")
fileVar.write("Line6\n") 
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'r')
print(fileVar.read()) #print the contents of the fileVar
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'a') #appends to old content
fileVar.write("Line7\n")
fileVar.write("Line8\n") 
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'r')
#fileVar.seek(0) #moves the pointer back to the beginning of the file
print(fileVar.read()) #print the contents of the fileVar
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'a')
list1 = ['LineA', 'LineB', 'LineC', 'LineD', 'LineE']
for item in list1:
    fileVar.write(item + '\n')
fileVar.close()

fileVar = open("C:\\out\\example_write.txt", 'r')
print(fileVar.read())
fileVar.close()