# # Functions - first class objects
# # Functions created using the "def"
# # declaration syntax
# # def <Identifier> (<argList>):
#     # Function Body

# def sayHi():
#     print("HI my name is vicky hajong")

# sayHi()

# def function_returns_value():
#     print('Inside :' , function_returns_value.__name__)
#     return "Hi kaise ho !!!"

# print(function_returns_value())

# #functions are objects and can be assignes like all other objects
# fn2 = sayHi
# fn2()

# #delete the object
# del sayHi
# print(type(fn2)) #shows the type of the object
# print(fn2) # see what it prints!!

# #Arguments in the function
# def fn_with_args(arg1, arg2):
#     print('Arg 1:', arg1, 'Arg2:',arg2)
#     return arg1+arg2
# result = fn_with_args(10,20)
# print(result)
# result = fn_with_args([1,2,3],[4,5,6])
# print(result)
# result = fn_with_args("Hello ","World")
# print(result)

# def fn_with_default_args(arg1 = 10,arg2 = 20):
#     print('Arg 1:', arg1, 'Arg 2:',arg2)
#     return arg1+arg2

# result = fn_with_default_args()
# print(result)
# result = fn_with_default_args(999)
# print(result)
# result = fn_with_default_args(666,666)
# print(result)

# def fn_with_variable_args(args1=0, *args):
#     print('Args 1 :', args1, "Other Args: ", args)

# fn_with_variable_args(100,True,10.22,'String','Anything else')

# def print_In(*args):
#     string = ""
#     for x in args:
#         string+=str(x) + ' '
#     print(string)

# print_In("A", 10, "B", True)

# def fn_with_list_args(arg1=0,args=[]):
#     print(args)
#     if(arg1 not in args):
#         args.append(arg1)
#     sum=0
#     for x in args: sum+=x
#     print(sum)

# fn_with_list_args(10)
# fn_with_list_args(20)
# fn_with_list_args(30)

# #Arguments are created before functions are called
# #Set default argument value as None to nullify this behaviour
# def fn_with_list_args2(arg1=0,args=None):
#     if(args is None):
#         args = []
#     print(args)
#     if(arg1 not in args):
#         args.append(arg1)
#     sum=0
#     for x in args: sum+=x
#     print(sum)
    
# fn_with_list_args2(10)
# fn_with_list_args2(20)
# fn_with_list_args2(30)

#Functions as arguments
'''----------------------------------------------------------------------------------'''
# def sum(arg):
#     return arg

# def aggregate(fnArg, *arg):
#     #print(fnArg(arg))
#     sum = 0
#     for x in arg:
#         sum+=fnArg(x)
#     print(sum)

# aggregate(sum,10,20,30,40)

# nested functions

# def Outer():
#     def Inner():
#         print('Inner')
    
#     Inner()
#     print("Outer")


# Outer()

# def Outer2():
#     def Inner():     #Inner is in local scope so it doesnt pollutes the whole code.multiple inner function can be defined when not in same scope
#         print('HUHUEHEUHEUHEUEH ')
#     Inner()
#     print('ODOOWDIOWDOWOD')

# Outer2()




## Higher order Functions
# def discount(itemcode):
#     def hasDiscount():
#         return 0.50
#     def nodiscount():
#         return 0.0
#     if(itemcode.startswith('a')):
#         return hasDiscount
#     else:
#         return nodiscount

# result = discount('a')
# print(result())
# print(discount("a"))   #both prints same result

# #recursion is allowed

# def recursive(n):
#     if(n==0): return 0
#     return  n+recursive(n-1)
# print('Recursive calls', recursive(4))
 #recursion depth value by default is = 1000 but u can change it 
''' -------use this  to change the set or get the limit----------
            from sys import getrecursionlimit, setrecursionlimit
            print(getrecursionlimit())
            setrecursionlimit(2000)
            print(getrecursionlimit())'''



# lambdas
# -- small anonymous function - usually single line functions

def capitalize(text):
    return text.capitalize()

names = ["benGALuru","chENnai","hyderaBAD"]

def editNames(fnArg, list):
    for x in list:
        print(fnArg(x))


def upperCase(text):
    return text.upper()

editNames(capitalize,names)
editNames(upperCase,names)
editNames(lambda a:a.swapcase(),names)










