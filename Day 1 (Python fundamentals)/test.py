'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
#name = input("Enter your name: ")
#print("you entered ", name)

#age = input("Enter your age: ")
#print("your age is ", age)
#age = int(age)+10
#print(age)

print(10**2)

print(10>>2)
print(10<<2)
print(10&2)
#print(10&&2)
print(True and True)
print(True and False)

# python constructors
a=10
if(a==11):
    print("a is 10")
    print("Next statement in the if block")
else:
    print("a is greater than 10")
print("after the if block")

# print greatest of the two numbers

#a = input("Enter the first number: ")
#b = input("Enter the second number: ")

#if(a>b):
 #   print(a)
#else:
#   print(b)

a = (input("Enter the first number: "))
b = (input("Enter the second number: "))
c = (input("Enter the third number: "))


if(int(a)==int(b) and int(a)==int(c)):
    print("All are equal")
elif(int(a)==int(b) and int(c)>int(a)):
    print("A and B are equal and c is larger")
    print(c)
elif(int(a)==int(b) and int(c)<int(a)):
    print("A and B are equal and c is smaller")
    print(a)
elif(int(a)==int(c) and int(b)>int(c)):
    print("A and C are equal and B is larger")
    print(b)
elif(int(a)==int(c) and int(b)<int(c)):
    print("A and C are equal and B is smaller")
    print(a)
elif(int(b)==int(c) and int(a)>int(c)):
    print("A and C are equal and A is larger")
    print(a)
elif(int(b)==int(c) and int(a)<int(c)):
    print("A and C are equal and A is smaller")
    print(b)
else:
    print(c)

for x in "apples":
    print(x)
    
for num in range (6): print(num)
print(" ")
for num in range(10,20): print(num)
print(" ")
for num in range(10,100,3):
    print(num,end=",")
else:
    print("\nend of for")

a = "This Is A String"
print('Upper: ', a.upper())
print('Lower: ', a.lower())
print('Capitalize: ', a.capitalize())
print('Fold case: ', a.casefold())
# Find text in String
print("his" in a)
print("Find 'his':", a.find("his"))
print("Index of 'his'", a.index("his"))
# startwith, endwith

print("starts with:", a.startswith("This"))
print("ends with:", a.endswith("This"))

# Justfy the strings 
print('Center Justify,[',a.center(80), ']')
print('Left Justify,[',a.ljust(80), ']')
print('Right Justify,[',a.rjust(80), ']')
print("Alternate chars: ",a[::2])

# split and Join strings
words = a.split(" ") # returns an array of words
for x in words: print(x)
joined = ",".join(words)
print("joined", joined)
paragraph = '''this is a long story written across multiple lines,
The first line identifies the name of the story,
the second line identifies the objective behind the story,
To BE uploaded later....
'''

lines = paragraph.splitlines()
for line in lines: print(line)
# replace chars in the string
newStr = a.replace("h","Hi")
print('replaced: ',newStr)
print('Length of string', len(newStr), 'chars')

# Slicing of the string[start:stop]
print("From the 10 char till end: ",a[10: ])
print("From begining till 5th char: ", a[:5])
print("From 3rd till the 10th char:", a[3:10])
print("Last 5 char:", a[-5:])
print("Last 5 to 3 char: ", a[-5:-3])
print("Last 5 to +ve char: ", a[-3:1])


a = "This Is A String"
print('Upper: ', a.upper())
print('Lower: ', a.lower())
print('Capitalize: ', a.capitalize())
print('Fold case: ', a.casefold())
# Find text in String
print("his" in a)
print("Find 'his':", a.find("his"))
print("Index of 'his'", a.index("his"))
# startwith, endwith

print("starts with:", a.startswith("This"))
print("ends with:", a.endswith("This"))

# Justfy the strings 
print('Center Justify,[',a.center(80), ']')
print('Left Justify,[',a.ljust(80), ']')
print('Right Justify,[',a.rjust(80), ']')

# split and Join strings
words = a.split(" ") # returns an array of words
for x in words: print(x)
joined = ",".join(words)
print("joined", joined)
paragraph = '''this is a long story written across multiple lines,
The first line identifies the name of the story,
the second line identifies the objective behind the story,
To BE uploaded later....
'''

lines = paragraph.splitlines()
for line in lines: print(line)
# replace chars in the string
newStr = a.replace("h","Hi")
print('replaced: ',newStr)
print('Length of string', len(newStr), 'chars')

# Slicing of the string[start:stop]
print("From the 10 char till end: ",a[10: ])
print("From begining till 5th char: ", a[:5])
print("From 3rd till the 10th char:", a[3:10])
print("Last 5 char:", a[-5:])
print("Last 5 to 3 char: ", a[-5:-3])
print("Last 5 to +ve char: ", a[-3:1])
print("Alternate chars: ",a[::2])

for x in a[::3]:
    print(x)

#SET
# a = {1,2,3}
# a[0] = 100 # not allowed
# a.add(200)
# a.remove(1)

theList = ["apples,","oranges","mangoes"]
for item in theList:
    print(item,end=" ")
else:
    print()
theList[0]="berries"
print(theList)

numberList = list(range(0,50,2))
print(numberList)

print("Items between 10th and 15th position", numberList[10:15])
print("reverse item", numberList[-20:-1:2])

print("reverse a list: ", numberList.reverse())
numberList.sort(reverse= True)
print("sort in ascending order", numberList)
numberList.sort(reverse= False)
print("sort in descending order", numberList)
# add items to the list
# append, extend, insert, +
newList = theList + ["chocolates", "pastries","Sweets"]
print(newList)
theList.append("chocolates")
print("Appending: ", theList)
theList.append(["pastries","Sweets"])
theList.extend(["pastries","Sweets"])
#remove items from the list
# remove, pop
theList.remove("pastries")
print(theList)
popped=theList.pop(2)
print("popped: ",popped, "The list:", theList)












