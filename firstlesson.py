print("Hello World") 
userName = input ("Enter your name:")
print ("Good morning", userName)

print ("Welcome!")
firstName = input ("Enter your first name:")
lastName = input ("Enter your last name:")
total = firstName + lastName 
print ("total", total)
print ("Good morning", lastName + firstName)

firstNumber = int(input ("Enter your first number:"))
secondNumber = int(input ("Enter your second number:"))
result = firstNumber - secondNumber
print ("Your result is:", result)

num1 = float(input ("enter your first number:"))
num2 = float(input ("enter your second number:"))
average = (num1 + num2)/2
print("your result is:", average)

#this is to show how computer calculates logs
import math
num3 = float(input("enter your number:"))
print("the log is:", math.log10(num3))

#this is to show a random nuber guessing generator 
# to create comment do comand, question mark 

import random 
PI = 3.14 #this is a constant that never changes

secretNumber = random.randit (1,10)
userGuess = int(input("enter your guess:"))
if userGuess == secretNumber: 
    print ("you won!")
else: 
    print ("you lose!")


#this is to show greater than or equal to

userGuess = int(input("what is your age:"))
VOTING_AGE = 18
if userGuess >= secretNumber: 
    print ("you won!")
else: 
    print ("you lose!")

#using elif function
userScore = float(input("enter your score:"))
if userScore >= 80: 
    print ("A")
elif 50<=userScore<= 79: 
    print ("B")
else: 
    print("F")


#practice 
#enter value and determine whether it is positive, zero, negative 


userValue = float(input("enter your number to be determined:"))

if userValue>0:
    print ("your number is positive!!")
elif userValue <0:
    print ("your number is negative, sorry!")
elif userValue == 0:
    print ("your number is a big fat ZERO")
# or else:
    # print ("your number is a big fat ZERO")



#using fall loops 
for i in range (5):
#when you say range any number it creates a list form 0 until the number before it. so [0,1,2,3,4]
    print("hello world!")


#print the first 100 even numbers 
for i in range(100):
    print(i*2)

for i in range(100):
    if i%2==0: 
        print (i)

#range (a, b, c)
# a= starting number
#b = ending number (so 9 if it is from 1-10)
#1<=x<9
#c = the number of steps in each jump so in this case 1 

for i in range(1,10,2):
    print (i) 

for i in range(11):
    if i%2!= 0:
        print(i) 

#using while loops (these are also infinite loops)
i = 0 
while i<5:
    print (i)
    i = i+1
#to kill this program you do command c 


#using while loops for our guess the number game

while userGuess != secretNumber:
    print ("guess again")
    secretNumber = int(input("enter your guess:"))
print("you're right!")

# importing the random library 
import random 
secretNumber = random.randint (1,10)
userGuess = int(input("guess my number"))
while userGuess != secretNumber:
    print ("guess again")
    secretNumber = int(input("enter your guess:"))
print("you're right!")






















