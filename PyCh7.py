# # The code below are examples of exception handling used in Python
# # See if you can follow each line of code.  I encourage you to add
# # comments to help remember what is happening on each line of code.
# # If you want to test any section of code, you will need to 
# # uncomment it.

# #Example 1
# try:
#   print(hello)
# except SyntaxError as e:
#   print("Invalid syntax")
# except:
#     print("Invalid syntax")

# #Example 2
# try:
#   print(a+b)
# except:
#   print("exception occured")

# #Example 3
# try:
#   print(x)
# except TypeError:
#   print("x is not defined")
# except:
#   print("Error")

# #Example 4
# try:
#    file = open("AllHomeworkSolutionsCHEE205.txt", "w")
#    file.write("This is the test file")
# except IOError:
#    print("No file found")
# else:
#    print("The content is not written in the file")
#    file.close()

# #Example 5
# try:
#   print(x)
# except:
#   print("x is not defined")
# finally:
#   print(" The finally is executed")

# #Example 6
# number = 2
# if number < 36:
#     raise ValueError('The given number is less than 36')

# #Example 7
# num = "python"
# if not type(num) is int:
#   raise TypeError("Only integers are allowed")

# #Example 8
# Rate = { 'bottle' : 5, 'chair' : 1200, 'pen' : 50}
# item = input('Enter the item: ')
# try:
#    print(f'The rate of {item} is {Rate[item]}')
# except KeyError:
#     print(f'The price of {item} is not found')

# #Example 9
# try:
#     inp = input("Enter the input:")
#     print ('Press Ctrl+c')
# except KeyboardInterrupt:
#     print ('Caught KeyboardInterrupt')
# else:
#     print ('No exception occurred')

# #Example 10
# i=1
# try:
#   num = 2.5**i
#   for i in range(20):
#       print(i, num)
#       num = num**8 
# except OverflowError as e:
#           print('Overflowed after ', num, e)

# #Example 11
# try:
#     list = [1,2,3,5,6,7]
#     print(list[8])
# except IndexError as e:
#     print(e)
# print("index error")

# #Example 12
# try:
#     print(cat)
# except NameError:  
#     print ("NameError:'cat' is not defined")
# else:  
#     print ("word found no error")

# #Example 13
# import sys
# try:
#     from cv import math
# except Exception:
#     print("improper module")

# #Example 14
# try:  
#     a = 5
#     b = 5
#     assert a != b
# except AssertionError:  
#         print ("Exception Error")
# else:  
#     print ("Success, no error!")

# #Example 15
# class Attributes(object):
#     num = 5
#     print(num)
# try:
#     object = Attributes()
#     print (object.attribute)
# except AttributeError:
#     print ("Attribute Exception")

# #Examples were borrowed from:
# #https://pythonguides.com/python-exceptions-handling/
