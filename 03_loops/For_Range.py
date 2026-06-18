# for..in ---> loop is used to go through each item in a sequence(list,string,tuple...etc) one by one
                            #example-1: for...in loop example
print("--------------------------------------------------------------------------------------------------")
fruits=["apple","banana","manga","orange"]
for fruit in fruits:
    print(fruit)
    
print("--------------------------------------------------------------------------------------------------")
                        #example-2: sorting and printing each item in list
nums=[1,55,3,6,85,2,78,29]
nums.sort()
for num in nums:
    print(num)
    
print("---------------------------------------------------------------------------------------------------")
#for...in with range(start,stop)-->generates an immutable sequence of integers dynamically which is used to control the number of iteration in a for loop
                            #example-3:range(start,stop)
for i in range(1,8): #here 8 is not included it only loops 8-1 times means 7 times
    print(i)
    
print("----------------------------------------------------------------------------------------------------")

                                #example-4:range(stop)

for j in range(8):
    print(i)