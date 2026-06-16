#random module create unpredictable behaviors in program
import random 
#example 1 :random.randint(a,b) // for int values
head_tails= random.randint(0,1)
if head_tails==1:
    print("heads")
else:
    print("tails")
    
#example 2: random.random()*num //for float values
num=random.random() * 8
print(round(num,2))

#example 3 : random.choice(list) // it gives a random value from a list
names = ['Robert', 'Steeve', 'Tom', 'Happy', 'Bruce']
chosen_one = random.choice(names)
print(f"{chosen_one} has to Pay the Bill")
