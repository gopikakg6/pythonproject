from sys import argv
script,filename=argv
txt=open(filename)
print(f"here is your {filename} ")
print(txt.read())
print("print the file name again ")
file_again=input(">")
txt_again=open(file_again)
print(txt_again.read())