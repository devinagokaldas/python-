# open other texts and strip the lines since an extra line gets added, and loop through each line
fhand = open('textFile.txt')
for line in fhand: 
    line = line.rstrip()
    line = line.upper()
    print(line)


fhand = open('textFile.txt')
for line in fhand: 
    line = line.rstrip()
    print(line)

# adding count variable 
count = 0 
for line in fhand: 
    count += 1 
print(count)


for line in fhand:
    line = line.rstrip()
#if you dont strip you get the accurate number bc on the txt file it doesn't show the \n after each line but it is there and that is counted as a character 
    for char in line:
        count+= 1 

for line in fhand: 
    if line.startswith("From:"):
        print (line)

for line in fhand: 
    if line.find("uct.ac.za") == -1: 
        continue
print(line)

# writing mode (w)
fhand = open("myfile.txt", "w")
fhand.write ("My favourite food is pasta")

# appendingmode (a), by adding what you want to what you already have 
fhand = open("myfile.txt", "a")
fhand.write ("My favourite food is pasta")


fhand = open("textFile.txt")
count = 0 
spamtotal = 0 

for line in fhand: 
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1 
        sppos = line.find(":")
        extract = line[sppos+2:]
        extract = float(extract)
        spamtotal += extract

average = spamtotal/count 
print(average)





