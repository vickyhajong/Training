# Dictionaries =  Key-Value Pairs
# - ordered (3.7>), mutable/changeable,non- duplicating keys
# Keys are usually strings - can be integers/boolesn/...

empty_dict = { }
print(empty_dict)
theDict = {"Header":"This is page Header","PageTitle":"This is page title","SectionTitle":"This is section title"}

print(theDict)
for x in theDict:
    print('Key: ',x,'Value:', theDict[x])

theList = [(1,'Hydrogen'),(2,'Helium'),(3,'Lithium')]
theElements = dict(theList)
print(theElements.keys(),theElements.values())

theTuple = ([1,'Bhawana'],[2,'Prashant'],[3,'Vicky'])
theElements2 = dict(theTuple)
print(theElements2.keys(),theElements2.values())

theList2 = ['ab','cd','ef']
theDict2= dict(theList2)
print(theDict2)
otherElements = {4: 'Berylium' , 5: 'Boron'}
theElements.update(otherElements)
print(theElements)

print('Get Item: ', theElements[1])   #Item key does not exist - throws exception
print('Get Item: ', theElements.get(6,'Nahi mill rha hai!!!!'))  #if item key does not exist , returns the default value

#remove all items from the dict
otherElements.clear()
#remove items from the dict using pop or popitem
theElements.pop(1) #key
print(theElements)
popped = theElements.popitem() # the last added item will get popped
print("popped : ",popped,"\nRemaining Elements : " ,theElements)

