num=int(input("enter the limit "))
for i in range(0,num):
    for j in range(0,i+1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

# num=int(input("enter the limit "))
# for i in range(num,0):
#     for j in range(0,i+1):
#         print(end=" *")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()