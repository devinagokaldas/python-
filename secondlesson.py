# creating a function to find the averageof 2 numbers 

def myaverage(a,b):
    return (a+b)/2


num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))

print("Average is", myaverage(num1,num2))


# create a function called say hello, has to accept a persons name then it has to say "Hello that persons name"

def sayhello (personname):
    return f"Hello {personname}"

Person = input("What is your name?")

print(sayhello(Person))


#lists using indexes to obtain certain values of the list 
ages = [3,6,9]

# this would be for the first age, in this case 3, as indexes start froom 0 
myage = ages[0]

# using fall loops to loop through each age
for i in ages:
    print (i)

for i in range(len(ages)):
    print(ages[i])
    
i = 0 
while i < 3: 
    print(ages[i])
    i +=1 

# 
scores = []
userScore = int(input("Enter score:"))
scores.append (userScore)

while True: 
    userScore = int(input("Enter score:"))
    if userScore <0:
        break
    scores.append (userScore)


print (f"done\n{scores}")


scores = []
userScore = int(input("Enter score:"))
scores.append (userScore)

while True: 
    userScore = int(input("Enter score:"))
    ans = input("Do you want to add this score to your list:")
    ans = ans.lower()
# this makes the input lowercase then we can check it
    if ans == "Y":
        scores.append (userScore)
    else: 
        continue
print (f"done\n{scores}")





