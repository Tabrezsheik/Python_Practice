num = input("enter a Value: ")
if not type(num) == type("hello"):
        if int(num) >0:
            print(f"Is an positive number : {num}")
        elif int(num) <0:
            print(f"Is an Negative number : {num}")
        else:
            print(f"Imaginary Numbers")
else:
    print("enter valid number")