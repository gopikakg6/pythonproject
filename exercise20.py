from sys import argv
script,input_file=argv
def print_all(file):
    print(file.read())
def rewind(file):
    file.seek(0)
def print_a_line(line_count,file):
    print(line_count,file.readline())
current_file=open(input_file)
print("first let print whole file :\n")
print_all(current_file)
print("now let's rewind ")
rewind(current_file)
print("let's rewind three lines :")
current_line=1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line,current_file)
current_line=current_line+1
print_a_line(current_line,current_file)

