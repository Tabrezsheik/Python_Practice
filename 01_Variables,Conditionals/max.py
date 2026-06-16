num= int(input("Enter the number of values to compare for min and max? :  "))
values=[]
for i in range(1,num +1):
    user_input = int(input("enter a value:  "))
    values.append(user_input)
max = 0
for com in values:
    for j in values:
        if com > j:
            max = com
        
print(f"the maximum values is: {max}")

