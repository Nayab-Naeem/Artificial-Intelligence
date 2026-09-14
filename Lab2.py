#while loop

count = 0
while (count <3):
    count = count +1
    print ("Hello Nayab")

# for loop
    
    print ("List Iteration")
    l = ["greeks", "for", "greeks"]
    for i in l :
        print (i)

 # Iterating over a String

s = "greeks"
for i in s :
    print (i)       

 # Iterating by index
  
list = ["apple", "graphs", "banana"] 
for index in range(len(list)):
    print ( list[index] )  

 # Print all letters except 
for letter in 'Artificial Intelligence is leading the modern technology':

    if letter == 'e' or letter =='s':
        continue

    print ('Current Letter :' , letter )


print ('Break Statement')

for letter in 'geeksforgeeks':

    if letter == 'e' or letter == 's': 
        break
    print ( 'Current Letter :', letter )


print ('Function Practice')
def fruit_shop(food):
 for x in food:
  print(x)

fruits = ["apple", "banana", "cherry" , "orange", "strawberry"]
fruit_shop(fruits)


#class creation
print ('Class Creation')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person ("Nayab" , 20)
print (p1.name)
print (p1.age)


#object Methods 

class Person:
   def __init__ (self, name, age):
       self.name = name
       self.age = age
   def namecall(self):
       print("Hello my name is " + self.name)
p1 = Person("Nayaabbb", 20)
p1.namecall()