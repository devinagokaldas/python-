fullname = input("Enter your full name: ")

for char in fullname: 
    if char.isupper():
        replacement = "_" + char.lower()
        fullname = fullname.replace(char, replacement)

print("snake case: ", fullname)

text = input("Enter any word: ")
vowels = "aeiouAEIOU"
for char in text: 
    if char in vowels :
        text = text.replace(char, "")

print(text)


# excersize 3
emails = {}

fhand = open("textFile.txt")
for line in fhand: 
    line = line.rstrip()
    if line.startswith("From "): 
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

print(emails)

# excersize 4

maxemails = 0 
target = None

for key,value in emails.items():
    if value > maxemails: 
        maxemails = value  
        target = key 

print("Maximum: ", target, emails[target])

minemails = 10
targeti = None

for key,value in emails.items():
    if value < minemails: 
        minemails = value  
        targeti = key 

print("Minimum: ", target, emails[targeti])



# excersize 5 

emails = {}

fhand = open("textFile.txt")
for line in fhand: 
    line = line.rstrip()
    if line.startswith("From "): 
        email = line.split()[1]
        at = email.split("@")
        extract = at[1]
        emails[extract] = emails.get(extract, 0) + 1

print(emails)


# On that note, implement a program that expects the name of a python file as
# input and outputs the number of lines of code in that file, excluding comments
# # and blank lines. If the specified file’s name does not end in .py, tell the user that
# # the file is not a python file.

programname = input("Enter the name of a python file: ")
while True: 
    if ".py" not in programname: 
        print("The file is not a python file")
        programname = input("Enter the name of a python file: ")
    else:
        break 

fhand = open(programname)
count = 0 
for line in fhand: 
    line = line.strip()
    if "#" in line or line == "": 
        continue 
    else: 
        count += 1 

print("There are", count, "number of lines of code in this file")


