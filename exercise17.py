from os.path import exists
file1=input("from which file that you are trying to copy :")
file2=input("enter the file to copy ")
file1_open=open(file1)
file_read=file1_open.read()
file_length=len(file_read)
print("length of the file {file1} {file_length}")
file_exists=exists(file2)
print(file_exists)
file2_open=open(file2,'w')
file2_open.write(file_read)
file1_open.close()
file2_open.close()