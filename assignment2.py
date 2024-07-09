# 1. Ask the user to type in their favorite school subject. Display it with “-“after each letter, e.g S-p-a-
# n-i-s-h-.

userFav = input("What is your favourite school subject?:")

print('-'.join(userFav) + '-')
print(userFav, end="-")


# 2. Ask the user to enter their first name. If the length of their first name is under five characters,
# ask them to enter their surname and join them together (without a space) and display the name
# in upper case. If the length of the first name is five or more characters, display their first name in
# lower case.

userFirstname = input("What is your first name?:")
 
if len(userFirstname) < 5:
    userLastname = input("Enter your surname: ")
    fullname = userFirstname + userLastname
    print(fullname)
else:
    print(userFirstname.lower())


# 3. Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an ‘ay’.
# If the word begins with a vowel, you just add “way” to the end. For example, pig becomes igpay,
# banana becomes ananabay, and aardvark becomes aadvarkway. Create a program that will ask
# the user to enter a word and change it into Pig Latin. Make sure the new word is displayed in
# lower case.



# 4. Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again.
# Keep repeating this until they type in a message all in uppercase.

userWord = input("Enter a word in uppercase: ")

while True: 
   if userWord == userWord.lower():
      print("Try again")
      userWord = input("Enter a word in uppercase: ")
   else: 
      break 


# 5. Ask the user to type in their name and then tell them how many vowels are in their name.

userName = input("What is your name?: ")
vowelcount = 0 
vowels = "aeiou"

for letter in userName:
    if letter in vowels:
        vowelcount += 1 
print("You have", vowelcount, "vowels in your name. ")



# 6. Ask the user to enter a new password. Ask them to enter it again. If the two passwords match,
# display “Thank you”. If the letters are correct but in the wrong case display the message “They
# must be in the same case”, otherwise display the message “Incorrect”.

userPassword = input("Enter a new password: ")
userPassword2 = input("Please enter it again: ")

if userPassword == userPassword2:
    print("Thank you")
elif userPassword == userPassword2.lower() or userPassword == userPassword2.upper():
    print("They must be in the same case")
else:
    print("Incorrect")

# 7. Ask the user to type in a word and then display it backwards on separate lines. For instance, if
# they type in “Hello” it should display as shown below:

userword = input("Type in a word:")

for letter in userword[::-1]:
    print(letter)

# 8. Come up with your own function which you can call delete_punctuation() this function takes
# in a string as input and removes all punctuation marks and returns the resulting string, now
# punctuation-free.

import string 
puncs = string.punctuation

def delete_punctuation(s):
   result = " "
   for char in s: 
       if char not in puncs: 
           result += char 
   return result 

inp = input("Enter something: ")
ans = delete_punctuation(inp)
print (ans)


