from sys import argv
script,filename=argv
print(f"we are going to erase {filename}.")
print("if you don't want that ,hit CTRL-C (^c).")
print("if you do want that ,hit RETURN")
input("?")
print("opening the file.......")
target=open(filename,'w')
print("truncating the file ...good bye :(")
target.truncate()
print("plz enter new lines ")
line1=input("line 1 :")
line2=input("line 2 :")
line3=input("line 3 :")
print("ok..iam going to write these lines to the file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("now im going to close the file")
target.close()


