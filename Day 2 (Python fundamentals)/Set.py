# Set - mutable,unordered collection of keys
# denoted by using { }

theSet = set("aaaeioubdcjklghzs")
print(theSet)
theList = list("aaaeioubdcjklghzs")
print(theList)
theSet.add("A")
print(theSet)
theSet.remove("a")
item = theSet.pop()
print('Popped', item, '\nThe Set' , theSet)
# Changing the item value is not allowed in the set , unlike list
#theSet[1]='Q'
theSet.add(5)
theSet.add(5)
theSet.add(5)
print(theSet)


#################################################################################

even_numbers = set(range(0,10,2))
odd_numbers = {1,3,5,7,9}
prime_numbers = {1,2,3,5,7,11}

#SET OPERATIONS : Intersection,Union,Difference
intersection = odd_numbers.intersection(prime_numbers) 
print(intersection)
intersection = odd_numbers & prime_numbers
print(intersection)

all_numbers  = odd_numbers.union(even_numbers)
print(all_numbers)
all_numbers =  odd_numbers | even_numbers | prime_numbers
print(all_numbers)

difference  = all_numbers.difference(prime_numbers)
print(difference)
difference = all_numbers - odd_numbers
print(difference)

# Subsets, Superset

print('even_numbers is a subset of all_numbers',even_numbers <= all_numbers)
print('even_numbers is a subset of all_numbers',even_numbers.issubset(all_numbers))

print('all_numbers is a superset of even_numbers',all_numbers >= even_numbers)
print('all_numbers is a superset of even_numbers' ,all_numbers.issuperset(even_numbers))

# Sets - unchangeable,unordered , non - duplicating collection of keys