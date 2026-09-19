#LAB2

#TASK 1 :

# 1.WHILE LOOP:

count = 0
while(count<3):
    count = count + 1
    print("Hello While loop!")
    
    #THIS CAN ALSO BE DONE IN SINGLE STATEMENT
#count = 0
#while(count==0):print("Hello World!")
    #this will give an infinite loop beacuse its always true

#2. FOR LOOP:

print("List Iteration")
l = ["Time","is","Money"]
for i in l:
    print(i)

#Iterating over a tuple
print("\nTuple Iteration")
t = ("Geeks","for","geeks")
for i in t:
    print(i)

#iterating over a string
print("\nString Iteration")
s = "ARTIFICIAL!"
for i in s:
    print(i)

#TASK 2:
#1.ITERATING BY INDEX OF SEQUENCE:

list = ["Artificial","Intelligence","labs"]
for index in range(len(list)):
    print(list[index])
    
#2. CONTINUE STATEMENT:

#print all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter=='e' or letter=='s':
        continue
    print('Current Letter:',letter)
    var = 10

#3.BREAK STATEMENT:
for letter in 'Timeismoney':
    #break the loop as soon as it sees 'e' or 's'
    if letter=='e' or letter=='s':
        break
    print('Current Letter:',letter)

#TASK 3:
#FUNCTIONS!:

#1.CREATING AND CALLING A FUNCTION:
print("FUNCTIONS IN PYTHON!!!")
def my_function():
    print("Hello! My Function:)")
my_function()

#2. FUNCTION PARAMETERS:
def my_fun(fname):
    print(fname + "flies")
my_fun("Buuter")
my_fun("Dragon")
my_fun("Fire")    

#3.PASSING DEFAULT PARAMETER 
def function(country = "PAKISTAN"):
    print("I AM FROM "+ country)
function("AMERICA")
function()
function("CANADA")

#4. PASSING LIST AS A PARAMETER
def list(food):
    for x in food:
        print(x)
fruits = ["Apple", "Banana", "Grapes", "Cherry"] 
list(fruits)

#5.RETURN VALUES FUNCTION
def fun(x):
    return 7*x
print(fun(2))
print(fun(11))
print(fun(17))

#6. KEYWORD ARGUMENTS
def key(child3, child2, child1):
    print("The youngest child is " + child3)
key(child1="Tom", child2="John", child3="Emma")

#TASK 4
#PYTHON CLASSES:
print("PYTHON CLASSES!!!!")
#1. CREATE A CLASS AND A OBJECT:
class My_class:
    x = 5
O1 = My_class()
print(O1.x)

#2. THE _INIT()_FUNCTION:
class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
P1= Person("Tom ", 28 )
print(P1.name)
print(P1.age)

#3.OBJECT METHODS
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def my_fun(self):
        print("Hello! My name is " + self.name)
        print("My age is " + str(self.age))
P2 = Person("Fajar ", 20 )
P2.my_fun()

        
