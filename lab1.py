#TASK 1:

x = 1
# The initial value of x is 1.
if x > 0:
    print("These are two comments")  # print a string.


#TASK 2:

print("Statement 1")
print("Statement 2")

# You can write the above two statements in the following way:
print("Statement 1"); print("Statement 2")


#TASK 3:

x = 1
if x > 0:
 print("This statement has a single space indentation")
 print("This statement has a single space indentation")

x = 1
if x > 0:
    print("This statement has a single tab indentation")
    print("This statement has a single tab indentation")

x = 1
if x > 0:
     print("This statement has single space+tab Indentation")
     print("This statement has single space+tab Indentation")


#TASK 4:

# 1. INTEGER TYPE
a = 1452
print(type(a))       

b = -4587
print(type(b))          

c = 0
print(type(c))          

# 2. FLOAT TYPE
g = 1.03
print(type(g))          

h = -11.23
print(type(h))          

i = 0.34
print(type(i))      

j = 2.12e-10
print(type(j))         

k = 5E220
print(type(k))        

# 3. COMPLEX TYPE
x = complex(1, 2)
print(type(x))          
print(x)               

z = 1 + 2j
print(type(z))        

# 4. BOOLEAN TYPE
x = True
print(type(x))         

y = False
print(type(y))          

# 5. STRING TYPE
str1 = "String"          # strings start and end with double quotes
print(str1)              

str2 = "String"
print(str2)              

str2 = 'Day"s'            # double quote within single quotes
print(str2)               

# 6. SPECIAL CHARACTERS IN STRINGS
print("THIS IS A BACKSLASH (\\) MARK.")


print("THIS IS TAB \t KEY.")


print("THESE ARE \'SINGLE QUOTES\'")


print("THESE ARE \"DOUBLE QUOTES\"")


print("THIS IS A NEW LINE \nNEW LINE")

#TASK 5:
#STRING INDICES AND ACCESSING STRING ELEMENTS

string1 = "PYTHON TUTORIAL!"
print(string1[0])     #PRINT FIRST CHARACTER

print(string1[-16])   #PRINT FIRST CHARACTER

print(string1[15])    #PRINT LAST CHARACTER

print(string1[-1])    #PRINT LAST CHARACTER

print(string1[3])     #PRINT FOURTH CHARACTER

print(string1[-13])   #PRINT FOURTH CHARACTER


#TASK 6:
#LISTS

my_list1 = [5, 12, 13, 14]   #the list contains integer values
print(my_list1)

my_list2 = ['red', 'blue', 'yellow', 'black']  #the list contains all string values
print(my_list2)

my_list3 = ['pink', 23, 13, 12.45]  #the list contains a string,integers and a float value
print(my_list3)

#LIST INDICES:

color_list = ['red', 'black', 'pink', 'purple', 'white', 'yellow']

print(color_list[0],color_list[5])  #print first and last element of the list

print(color_list[-3])  #return fourth element of the list

#LIST SLICE:

fruit_list = ['MANGO', 'CHERRY', 'APPLE', 'WATERMELON', 'STRAWBERRY' ]

print(fruit_list[0:3])   #CUT FIRST 3 ITEMS

print(fruit_list[1:2]) #CUT second ITEM

print(fruit_list[:4])  #CUT FIRST 4 ITEMS

print(fruit_list[1:-3])  #cut second item

print(fruit_list[:])   #CREATES COPY OF ORIGINAL LIST

#TASK 7

#CONDITIONAL STATMENTS:

num = 10
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
    
#WHICH NUMBER IS GREATER
#GET THREE NUMBERS FROM USER AS INPUT OF INTEGER TYPE
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)