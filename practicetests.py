# # 1. Ask the user to enter three numbers. Add together the first two numbers and
# # then multiply this total by the third. Display the answer as The answer is
# # [answer].

userNumber1 = float(input("enter your first number:"))
userNumber2 = float(input("enter your second number:"))
userNumber3 = float(input("enter your third number:"))

total = (userNumber1 + userNumber2)*userNumber3
print("The answer is:", total)

# # 2.Ask how many slices of pizza the user started with and ask how many slices
# # they have eaten. Work out how many slices they have left and display the
# # answer in a user-friendly format.

userOripizza = int(input("How many pizza slices did you start with?"))
userFinpizza = int(input("How many pizza slices have you eaten"))
total = userOripizza - userFinpizza
print("You have", total, "slices of pizza left")

# # 3.Ask for the total price of the bill, then ask how many diners there are. Divide
# # the total bill by the number of diners and show how much each person must
# # pay.

totalprice = float(input("What was the total price of the bill?"))
noofdinners = int(input("How many dinners were there?"))
total = totalprice/noofdinners
print("Each person must pay", total, "dollars")

# 20.Ask for a number below 50 and then count down from 50 to that number,
# making sure you show the number they entered in the output.


while True: 
        inputNum = int(input("Enter a number below 50:"))
        for i in reversed (range(inputNum,51)):
             print (i)


# 21.Set a variable called total to 0. Ask the user to enter five numbers and after
# each input ask them if they want that number included. If they do, then add
# the number to the total. If they do not want it included, don’t add it to the
# total. After they have entered all five numbers, display the total.

total = 0 

for i in range (5): 
    userNum5 = int(input("Enter a number:"))
    NumIncl = input("Do you want that number included?:") 
    NumIncl = NumIncl.lower()
    if NumIncl == "yes":
        total = total + userNum5
    else:
        continue 
print ("Your total is", total)


# 22.Ask which direction the user wants to count (up or down). If they select up,
# then ask them for the top number and the count from 1 to that number. If
# they select down, ask them to enter a number below 20 and then count down
# from 20 to that number. If they entered something other than up or down,
# display the message “I don’t understand”.

# userCount = input("What direction do you want to count (up or down): ")

while True: 
    if userCount == "up":
        topNumber = int(input("What is your top number?:"))
        for i in range(1,(topNumber+1)):
            print (i)
        break

    elif userCount == "down":
        bottomNumber = int(input("Enter a number below 20:"))
        for ii in reversed (range(bottomNumber,21)):
            print (ii)
# for i in range(20, (bottomNumber-1),-1):
# print (i)
        break 

    else: 
        print ("I don't understand")
        break 



# 23.Ask how many people the user wants to invite to a party. If they enter a
# number below 10, ask for the names and after each name display “[name]
# has been invited”. If they enter a number which is 10 or higher, display the
# message “Too many people”

partyInvite = int(input("How many people do you want to invite?"))

if partyInvite < 10:
    for i in range (partyInvite):
        Invited = input("What are the names?")
        Invited = Invited.lower()
        print(Invited, "has been invited")
else: 
    print ("Too many people")       


# 24.Set the total to 0 to start with. While the total is 50 or less, ask the user to
# input a number. Add that number to the total and print the message “The
# total is ... [total]”. Stop the loop when the total is over 50.

total = 0

while True:
    if total <= 50:
        userAns = int(input("Enter a number:"))
        total = total + userAns 
        print("The total is", total)
    else:
        break 



# 25.Ask the user to enter a number. Keep asking until they enter a value over 5
# and then display the message “The last number you entered was a [number]”
# and stop the program. 

list = []
userNum4 = int(input("Enter a number:"))
list.append (userNum4)

while True:
   if userNum4 <= 5:
    userNum4 = int(input("Enter a number:"))
    list.append (userNum4)
   else: 
    break 

print("The last number you entered was",userNum4)



# 26.Ask the user to enter a number and then enter another number. Add these
# two numbers together and then ask if they want to add another number. If
# they enter “y”, ask them to enter another number and keep adding numbers
# until they do not answer “y”. once the loop has stopped, display the total.

userNum = int(input("Enter a number:"))
userNum2 = int(input("Enter a second number:"))
ans = userNum + userNum2
while True: 
    Adding = input("Do you want to add another number?")
    Adding = Adding.lower()
    if Adding == "y":
        userNum3 = int(input("Enter another number:"))
        ans += userNum3 
    else:
        print("Your total is", ans)
        break



# # 27.Create a variable called compnum and set the value to a random number
# # between 1 and 20. Ask the user to enter a number. While their guess is not
# # the same as the compnum value, tell them if their guess is too low or too
# # high and ask them to have another guess. If they enter the same value as
# # compnum, display the message “Well done, you took [count] attempts”.

import random 

compnum = random.randint (1,20)
attempts = 1
userNumber = int(input("Enter a number:"))

while userNumber != compnum:
    if userNumber < compnum:
        print("Too low\nTry again")
        attempts += 1 
        userNumber = int(input("Enter a number:"))
    elif userNumber > compnum:
        print("Too high\nTry again")
        attempts += 1 
        userNumber = int(input("Enter a number:"))

print ("Well done, you took", attempts, "attempts")


# # 28.Ask the user to enter a number between 10 and 20. If they enter a value
# # under 10, display the message “Too low” and ask them to try again. If they
# # enter a value above 20, display the message “Too high” and ask them to try
# # again. Keep repeating this until they enter a value that is between 10 and 20
# # and then display the message “Thank you”.


userValue = int(input("Enter a value between 10 to 20:"))

i = userValue 
while i<10 or i>20: 
    if userValue <10:
        print("Too low\nTry again")
        userValue = int(input("Enter a value between 10 to 20:"))
    elif userValue >20:
        print("Too high\nTry again")
        userValue = int(input("Enter a value between 10 to 20:"))
    
print("Thank you")

# # or 

while True: 
    if userValue < 10:
        print("Too low\nTry again")
        userValue = int(input("Enter a value between 10 to 20:"))
    elif userValue > 20:
        print("Too high\nTry again")
        userValue = int(input("Enter a value between 10 to 20:"))
    else:
        print("Thank you")
        break 



# # 29.Make a math quiz that asks five questions by randomly generating two whole numbers to make the question (eg. [num1] + [num2]). 
# #Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got 
# #correct out of five.

import random

score = 0 

for i in range(5):
    num1 = random.randint (0,100)
    num2 = random.randint (0,100)
    correctAns = num1 + num2 
    userAnswer = int(input(f"{num1} + {num2} ="))
    
    if userAnswer == correctAns: 
        score = score + 1
    # or you can do this: score += 1  

print("You got" ,score, "out of 5")

