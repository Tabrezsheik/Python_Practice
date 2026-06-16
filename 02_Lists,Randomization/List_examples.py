#list Examples

#list example 1 :list.append(items) //add items to end of list 
fruits=['apples','banana','orange']
print(fruits )
fruits.append("mangos")
print(fruits)
print("-------------------------------------------------------------------------------------------------\n")

#list example 2 : list.pop(index) //it removes and returns items from list if u give index .
# If not provide index it will remove and return from end of list
animals=['cat',"dog","cow","rabbit","lion","goat","donkey"]
animals_1=animals.pop(3)
animals_2=animals.pop()
print(f"removed from given index 3: {animals_1}\nwithout index gives end element of list: {animals_2}")
print("----------------------------------------------------------------------------------------------------\n")

# length of a list len()
num =[1,2,3,4,5,88,99,22,11,23,35,64]
print(f"Length of list is {len(num)}")
print("---------------------------------------------------------------------------------------------------\n")
#list.sort() // sorts the list default ascending order if .sort(reverse==True) // descending order
num1 =[69,7,18,11,1,1,4,6,234,67]
num2 =[69,7,18,11,1,1,4,6,234,67]
num1.sort()
num2.sort(reverse = True)
print(f"values in Ascending order {num1}")
print(f"values in Descending order {num2}")
print("---------------------------------------------------------------------------------------------------------\n")

# .extend(list) //combines two lists
letters=['a','b','c','d','e']
letters_capital=['A','B','C','D','E']
letters.extend(letters_capital)
print(letters)
print("---------------------------------------------------------------------------------------------------------\n")

#.index(item) //returns items index position in list
birds=['eagle','parrot','sparrow','owl','falcon']
bird_index = birds.index("owl")
print(f"Index of owl is : {bird_index}") 

print("---------------------------------------------------------------------------------------------------------\n")


#nested list
names=[['Ironman','steeve'],['Batman','alfred']]
print(names[0]) #output :['Ironman', 'steeve']
print(names[0][1])#output steeve
print(names[1][0])#output Batman

