print("please select door #1 or door #2")
door=input(">")
if door=="1":
    print("you have two options\n\t1.take the bottle\n\t2.take the bat")
    option=input(">")
    if option=="1":
        print("fill the bottle")
    elif option=="2":
        print("play with this")
    else:
        print("you chose the wrong option")
elif door=="2":
    print("you have two options\n\t1.take the ball\n\t2.pick the flower")
    option=input(">")
    if option=="1":
        print("play with this")
    elif option=="2":
        print("feel it")
else:
        print("you chose the wrong option")
    