# round function
# 13.Ask the user to enter an integer that is over 500. Work out the square root of
# that number and display it to two decimal places.
# Hint: Check out from google or chatgpt what the round function is and how
# it can be used

import math
num = int(input("Enter a number above 500:"))
ans= math.sqrt(num)
print(round(ans,2))
print(f"{ans:.2f}")

# f strings (format strings)
uname = "Kofi" 
print("My name is {}".format(uname))

# 15.Display the following message:
# 1) Square
# 2) Triangle
# Enter a number:
# If the user enters 1, then it should ask them for the length of one of its sides
# and display the area. If they select 2, it should ask for the base and height of
# the triangle and display the area. If they type anything else, it should give
# them a suitable error message.

def squarearea(a):
    return (a**2)

def trianglearea(a,b):
    return (a*b)/2

userEnter = int(input("1) Square\n2) Triangle\nEnter a number:"))
if userEnter == 1:
    squareArea = float(input("What is the length of one of it's sides:"))
    print("Your area is", squarearea(squareArea))
elif userEnter == 2: 
    trianglebase = float(input("What is the base of your triangle:"))
    triangleheight = float(input("What is the height of your triangle:"))
    print("Your area is",trianglearea(trianglebase, triangleheight))
else: 
    print("Error, please try again")

# # strings - must always be integers(the indexes)
fruit = "banana"
letter = fruit[1]
# this would show "a"

fruit = "apple"
for letter in fruit: 
    print(letter)

# # or

for i in range(len(fruit)):
    print(fruit[i])

# # slicing words, so in this case you also do th number one above bc it starts from 0 
s = "Monthy Python"
print(s[0:5])

d = "Devina"
print(d[1:4])
# only woks when the starting index is 0
print(d[:3])
# this is not for a range but from 3 going
print(d[3:])
# this is when you're slicing the whole thing
print(d[:])
# writing it backwards
print(d[::-1])

# # immutable means you can't change the value of the string 
greeting = "Hello world"
new_greeting = "J" + greeting[1:]
print(new_greeting)

# # using count variable

word = "banana"
count = 0 
for i in range(len(word)):
    if word[i] == "a":
        count+=1 
print(f"a appears {count} number of times")


# create a function called count and it has to accept string and letter, count how many times that letter appeas in that string 


def count(a,b):
    count1 = 0 
    for i in range(len(a)):
        if a[i] == b:
            count1 +=1 
    return count1

wordB = input("What is your favourite fruit?:")
letter = input("What letter do you want to be checked?:")

ans = count(wordB,letter)
print("The letter", letter, "is repeated", ans, "times")

# # capitalize all, first letter, find

uname = "Devina"

uname.upper()
uname.lower()
uname.capitalize()
# find the posiion/index of it 
uname.find()
uname.count()

# revert it back to the original when there is extra spaces (before or after)
uname = uname.strip()
# strip everything on the right 
uname = uname.rstrip()
# strip everything on the left
uname = uname.lstrip()

line = "Have a nice day"
# check if it starts with lower case h 
line.startwith("h")

# # make the line lowercase then check if it starts with lowercase h
line.lower().startwith("h")

# # finding a certain part of an email

Email = "devinagokaldas@uct.ac.za Sunday 14th June 2008"

atpos = Email.find("a")
print(atpos)

sppos = Email.find(" ", atpos)
print (sppos)

store = Email[atpos+1:sppos]
print(store)

# find the portion of the string after the colon and then use float to convert the extracted into a floating point number

str = "X-DSPAM-Confidence: 0.8475"

sppos = str.find(":")
print(sppos)

number = str[sppos+2:]
print(number)

number = float(number)
print(number)





