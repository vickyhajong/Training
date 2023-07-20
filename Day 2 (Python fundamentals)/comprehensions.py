# Comprehensions - consise statements
# expression for identifier in collection if condition
# yields a new set/list/dict

numbers = list(range(1,20,1))
evenList =[]

for x in numbers:
    if(x%2 == 0):
        evenList.append(x)
print(f"Original list:  {numbers}")   #string interpolation
print("Even numbers: {0}".format(evenList))
print("Even Numbers: ", evenList)
# Another way to do that 

newList  = [ x for x in numbers if(x%2==0)]  #list comprehension
print(f"New List : {newList}")

matrix = [(row,col) for row in range (1,5) for col in range(1,5) if(row != col)]
print(f"Matrix: {matrix}")


aString = "Object Oriented Programming"
letterCount = { letter: aString.count(letter) for letter in aString}
print(f"Word Count\n {letterCount}")

#figure out how tuple comprehensions are done
