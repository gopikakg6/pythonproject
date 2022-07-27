fruits=int(input("enter the total no of fruits : "))
vegetables=int(input("enter the total no of vegetables : "))
flowers=int(input("enter the total no of flowers : "))
if fruits>100:
    print(f"there are {fruits} of fruits")
elif fruits<vegetables:
    print(f"the no of fruits are lesser than vegetables")
elif fruits==vegetables and flowers:
    print(f"there are equal no of fruits and vegetables ..ie,fruits={fruits}\n\t vegetables={vegetables}\n\tflowers={flowers}")
else:
    print(fruits,vegetables,flowers)