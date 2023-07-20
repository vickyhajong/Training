#Created using () notation
#Tuple values do not chamge
#Tuple - immutable collections

theTuple = (1,122324212,3,4)
print(theTuple)
print(theTuple[0])
newTuple = theTuple + (5,6,7)
print(newTuple)

print(theTuple.count(3))
print('Index',theTuple.index(3))
print('2 exists ', 2 in theTuple)

#Tupke - immutable, unchangeable, ordered 
# to extract the items from a tuple - deconstruct the tuple
(a,b,c,d) = theTuple

print('a:{0:.6f} ,b:{1:X}, c:{2} '.format(a,b,c))