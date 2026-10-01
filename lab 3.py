
# ----------------------------------------------------------------------
# Q1: Numbers divisible by 7 and multiple of 5, between 1500 and 2700
# ----------------------------------------------------------------------
print("Q1: Numbers divisible by 7 and multiple of 5 (1500-2700)")

result = []                      # empty list to store the answers
for num in range(1500, 2701):    
    if num % 7 == 0 and num % 5 == 0:   
        result.append(num)       # add number to the list if true

print(result)
print()


# ----------------------------------------------------------------------
# Q2: Convert temperature between Celsius and Fahrenheit
# ----------------------------------------------------------------------
print("Q2: Temperature Conversion")

celsius = 60
fahrenheit = (celsius * 9 / 5) + 32    
print(f"{celsius}C is {fahrenheit} in Fahrenheit")

fahrenheit2 = 45
celsius2 = (fahrenheit2 - 32) * 5 / 9   # Fahrenheit to Celsius 
print(f"{fahrenheit2}F is {celsius2} in Celsius")
print()


# ----------------------------------------------------------------------
# Q3: Guess a number between 1 and 9
# ----------------------------------------------------------------------
print("Q3: Guess the Number Game")

import random
number_to_guess = random.randint(1, 9)   # pick a random number between 1-9

while True:                              # keep asking until correct guess
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number_to_guess:
        print("You guessed right!")
        break                             # exit the loop, program ends
    else:
        print("Wrong guess, try again.")
print()


# ----------------------------------------------------------------------
# Q4: Print a pyramid pattern of stars using a nested for loop
# ----------------------------------------------------------------------
print("Q4: Star Pattern")

n = 5   # number of rows for the top half of the pattern

for i in range(1, n + 1):
    print("* " * i)

# Bottom half 
for i in range(n - 1, 0, -1):
    print("* " * i)
print()


# ----------------------------------------------------------------------
# Q5: Accept a word from the user and reverse it
# ----------------------------------------------------------------------
print("Q5: Reverse a Word")

word = input("Enter a word: ")
reversed_word = word[::-1]     # reverses the string
print("Reversed word:", reversed_word)
print()


# ----------------------------------------------------------------------
# Q6: Count even and odd numbers from a series of numbers
# ----------------------------------------------------------------------
print("Q6: Count Even and Odd Numbers")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)   

even_count = 0
odd_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1      # increase even counter
    else:
        odd_count += 1       # increase odd counter

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
print()


# ----------------------------------------------------------------------
# Q7: Print each item and its type from a list
# ----------------------------------------------------------------------
print("Q7: Print Items and Their Types")

datalist = [1452, 11.23, 1 + 2j, True, 'resource', (0, -1), [5, 12],
            {"class": "BSIT", "section": "M"}]

for item in datalist:
    print(item, "->", type(item))   # type() tells us the data type
print()


# ----------------------------------------------------------------------
# Q8: Print numbers from 0 to 6 except 3 and 6 (use continue)
# ----------------------------------------------------------------------
print("Q8: Print Numbers Except 3 and 6")

for i in range(0, 7):        
    if i == 3 or i == 6:
        continue              # skip the rest of the loop 
    print(i, end=" ")
print("\n")


# ----------------------------------------------------------------------
# Q9: Fibonacci series between 0 and 50
# ----------------------------------------------------------------------
print("Q9: Fibonacci Series (0 to 50)")

a, b = 0, 1                  # first two Fibonacci numbers
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b           # move to the next  numbers
print("\n")


# ----------------------------------------------------------------------
# Q9b: FizzBuzz (1 to 50)
# ----------------------------------------------------------------------
print("Q9b: FizzBuzz")

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print()


# ----------------------------------------------------------------------
# Q10: Generate a 2D array where element[i][j] = i*j
# ----------------------------------------------------------------------
print("Q10: 2D Array where value = i*j")

m = 3   # rows
n = 4   # columns

array_2d = []                   
for i in range(m):
    row = []                     #  one row at a time
    for j in range(n):
        row.append(i * j)       
    array_2d.append(row)

print(array_2d)
print()


# ----------------------------------------------------------------------
# Q11: Accept lines of text and print in lower case
# ----------------------------------------------------------------------
print("Q11: Convert Lines to Lower Case")

lines = []
while True:
    line = input("Enter a line (blank to stop): ")
    if line == "":            # blank line means stop taking input
        break
    lines.append(line.lower())   # convert to lower case 

for line in lines:
    print(line)
print()


# ----------------------------------------------------------------------
# Q12: From comma separated 4-digit binary numbers, print those divisible by 5
# ----------------------------------------------------------------------
print("Q12: Binary Numbers Divisible by 5")

sample_data = "0100,0011,1010,1001,1100,1001"
binary_numbers = sample_data.split(",")   # split into a list of strings

results = []
for b in binary_numbers:
    decimal_value = int(b, 2)     # convert binary string to decimal
    if decimal_value % 5 == 0:
        results.append(b)

print(",".join(results))
print()


# ----------------------------------------------------------------------
# Q13: Count the number of digits and letters in a string
# ----------------------------------------------------------------------
print("Q13: Count Digits and Letters")

text = "Python 3.2"

letters = 0
digits = 0
for ch in text:
    if ch.isalpha():          # checks if the character is a letter
        letters += 1
    elif ch.isdigit():        # checks if the character is a digit
        digits += 1

print("Letters", letters)
print("Digits", digits)
print()


# ----------------------------------------------------------------------
# Q14: Validate a password
# Rules:
#   - at least 1 lowercase letter [a-z]
#   - at least 1 uppercase letter [A-Z]
#   - at least 1 digit [0-9]
#   - at least 1 special character from [$#@]
#   - length between 6 and 16 characters
# ----------------------------------------------------------------------
print("Q14: Password Validation")

import re   # re = regular expressions, used for pattern matching

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password):     # needs a lowercase letter
        return False
    if not re.search("[A-Z]", password):     # needs an uppercase letter
        return False
    if not re.search("[0-9]", password):     # needs a digit
        return False
    if not re.search("[$#@]", password):     # needs a special character
        return False
    return True

test_password = input("Enter your password: ")
if is_valid_password(test_password):
    print(test_password, "is a valid password")
else:
    print(test_password, "is NOT a valid password")