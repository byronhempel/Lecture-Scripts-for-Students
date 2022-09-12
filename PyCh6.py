# # Example 1 of List Comprehension
# Ex1a = [i**3 for i in range (1,11)] #what does this line do?
# print(Ex1a) #what does this line do?
# Ex1b = [i**3 for i in range (11)] #what does this line do?
# print(Ex1b) #what does this line do?

# # Example 2 of List Comprehension
# Ex2 = [i**3 for i in [1,2,3,4] if i>2]
# print(Ex2)

# # Example 3 of List Comprehension
# Ex3 = [x**2 for x in range (0,50) if x % 3 == 0]
# print(Ex3)

# # MC1
# my_string = "batman123"
# k = [print(i) for i in my_string if i not in "aeiou"]
# print(k)

# # MC2
# my_string = "batman123"
# k = [i for i in my_string if i not in "aeiou"]
# print(k)

# # MC3
# my_string = "hello world"
# k = [(i.upper(), len(i)) for i in my_string]
# print(k)

# # MC4
# # creating a function, we'll learn how to do this later
# def expr(i): #this expression simply squares the number
#     new_i = i**2
#     return new_i
# #here is a generic list
# list_0 = [1,2,3,4]
# print(list_0)
# #the list comprehension
# list_1 = [expr(i) for i in list_0 if expr(i)]
# print("The list comprehension output is: %s" % list_1)
# #the loop version
# list_2 = []
# for i in list_0:
#     if expr(i):
#         list_2.append(expr(i))
# print("The loop output is: %s" % list_2)
# if list_1 == list_2:
#     print("yay they are the same!")
# else:
#     print("uhhh oh, something went wrong")

# # MC5
# x = [i**+1 for i in range(3)]; print(x);

# # MC6
# print([i.lower() for i in "HELLO"])

# # MC7
# print([i+j for i in "abc" for j in "def"])

# # MC8
# print([[i+j for i in "abc"] for j in "def"])

# # MC9
# #print([if i%2==0: i; else: i+1; for i in range(4)])
# print([i if i%2==0 else i+1 for i in range(4)]) #A
# print([i+1 if i%2==0 else i for i in range(4)]) #B

# # MC10
# import math
# print([str(round(math.pi)) for i in range (1, 6)]

# # MC11
# print([x for x in range(0, 20) if (x%2==0)])

# # MC12
# list_4 = []
# for i in range(1, 101):
# 	if int(i*0.5)==i*0.5:
# 		list_4.append(i)
# print(list_4)
# print([i for i in range(1, 101) if int(i*0.5)==(i*0.5)])

# # DC Example 1
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Double each value in the dictionary
# double_dict1 = {k:v*2 for (k,v) in dict1.items()}
# print(double_dict1)

# # DC Example 2
# # Python code to demonstrate dictionary 
# # comprehension
  
# # Lists to represent keys and values
# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  
  
# # but this line shows dict comprehension here  
# myDict = { k:v for (k,v) in zip(keys, values)}  
  
# # We can use below too
# # myDict = dict(zip(keys, values))  
  
# print (myDict)