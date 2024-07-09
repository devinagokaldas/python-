# # # # question 1 
# # principal = float(input("Enter the principal: "))
# # time = float(input("Enter the time: "))
# # rate = float(input("Enter the rate: "))

# # SI = (principal + time + rate)/100
# # print("The simple interest is", SI)


# # # # question 2 

# # value = float(input("Input your value (it is in Ghana Cedis): "))

# # dollar= value/16
# # print("$", dollar)

# # question 3 - fibbonaci 

# # # question 4

# # num = input("Enter a number: ")
# # if num[::-1] == num: 
# #     print("it is a palindrome")
# # else: 
# #     print("it is not a palindrome")


# # # question 5 

# # import math 
# # num1 = input("Enter a number: ")
# # numint = int(num1)
# # total = 0 

# # for digits in num1: 
# #     total+=int(digits)**len(num1)

# # if total == numint: 
# #     print("it is an armstrong number ")
    

# # # # question 6 

# def sum(num):
#     sum = 0 
#     for each in num: 
#         sum += int(each)
#     return sum

# def product(num):
#     product = 0 
#     for digit in num: 
#         product*=int(digit)
#     return product 

# num2 = input("Enter a number: ")
# mysum = sum(num2)
# myproduct = product(num2)
# ans = abs(myproduct - mysum)
# print(ans)



# # question 8


# num3 = float(input("Enter a number: "))
# sum = 0 

# while True: 
#     if num3 != 0: 
#         sum += num3
#         num3 = float(input("Enter a number: "))
#     else: 
#         break 

# print(sum)

# # question 9

# num4 = float(input("Enter a number: "))
# sum = []

# while True: 
#     if num4 != 0: 
#         sum.append(num4)
#         num4 = float(input("Enter a number: "))
#     else: 
#         break 

# print(max(sum))

# # question 10 - factorials 

# fact = int(input("Enter a number: "))
# factorial = 1

# if fact == 0: 
#     print("The factorial of ", fact, "is 1")
# else: 
#     for i in range(fact,0,-1):
#         factorial*= i

# print(factorial)

# # hailstone sequence 

# num = int(input("Enter a number: "))


# count = 0 

# while num != 1: 
#     if num%2 != 0: 
#         count +=1
#         num1 = 3*num + 1 
#         print(num, "is odd, so I make 3n + 1 = ", num1)
#         num = num1
#     elif num%2 == 0: 
#         count += 1 
#         num2 = num/2
#         print(num, "is even, so I take half= ", num2)
#         num = num2
    
    
# print("The process took", count, "steps to reach 1 ")


# num = input("Enter a number: ")
# secnum = input("Enter the number to be found: ")

# count = 0 
# for each in num: 
#     if each == secnum : 
#         count +=1 
# print (count)


def total(num):
    total - num 

while True: 
    print("There are", total(num1), "number of stones left")
    num1 = int(input("Player 1 would you like to remove 1 or 2 stones: "))
    print("There are", total - num1, "number of stones left")
    num2 = int(input("Player 2 would you like to remove 1 or 2 stones: "))
    print("There are", total - num2, "number of stones left")
    if total == 0: 
        print("PLayer  is the loser")








