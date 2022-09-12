# # Below are answers to the multiple choice questions in
# # lecture 13 - PyCh10 for CHEE 205.  

# # MC1 - importing from different modules
# import random
# random.seed()

# import math
# math.sqrt(36)
# math.factorial(4)

# #no import needed!
# print("I'm already here!!!")

# # MC2 - Round
# MC2_ans = round(4.576)
# print("Rounding the number gives %s." % MC2_ans)

# # MC3 - power
# x = 2
# y = 3
# z = 9
# help(pow)
# MC3_ans = pow(x,y,z)
# print("Using this funcion, the answer is %s." % MC3_ans)
# print("This is because when 2^3 / 9 = 0 r8.")

# # MC4 - all vs any
# MC4_ans = all([2,4,0,6])
# print("Using the all funcion, the answer is %s." % MC4_ans)
# MC4_ans2 = any([2,4,0,6])
# print("Using the any funcion, the answer is %s." % MC4_ans2)

# # MC5 - round
# MC5_ans = round(4.5676,2)
# print("Using the round funcion, the answer is %s." % MC5_ans)

# # MC6 - any
# MC6_ans = any([2>8, 4>2, 1>2])
# print("Using the any funcion, the answer is %s." % MC6_ans)

# # MC7 - abs and sqrt
# import math
# MC7_ans = abs(math.sqrt(25))
# print("With 2 sig figs, the answer is %s." % MC7_ans)

# # MC8 - sum function
# try: #first function
#     print(sum(2,4,6))
# except:
#     print("This doesn't work!")
# try: #second function
#     print(sum([1,2,3]))
# except:
#     print("This doesn't work!")

# # MC9 - all
# try: #first function
#     print(all(3,0,4.2))
# except:
#     print("This doesn't work!")

# try: #corrected
#     print(all([3,0,4.2]))
# except:
#     print("This doesn't work!")

# # MC10 - min and max
# MC10_ans = min(max(False,-3,-4), 2,7)
# print("The answer is %s." % MC10_ans)

# # Q13 - Hello
# def sayHello():
#     print('Hi!') 
# sayHello() 
# sayHello()

# # MC14 - printMax
# def printMax(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
# printMax(3, 4)

# # Q15 - func(x)
# x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)

# # Q16 - global x
# x = 50
# def func():
#     global x
#     print('x is', x)
#     x = 2
#     print('Changed global x to', x)
# func()
# print('Value of x is', x)

# # Q17 - say function
# def say(message, times = 1):
#     print(message * times)
# say('Hello')
# say('World', 5)

# # Q18 - func inputs
# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
 
# func(3, 7)
# func(25, c = 24)
# func(c = 50, a = 100)
# try: #trial
#     func(1,3,c=5)
# except:
#     print("This doesn't work!")
# finally:
#     print("See what happens when you change the inputs!")

# # Q19
# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'The numbers are equal'
#     else:
#         return y
 
# print(maximum(2, 3))

# # Q20 - Celsius to Fahrenheit
# def C2F(c):
#     return c * 9/5 + 32
# print(C2F(100))
# print(C2F(0))

# # Q20 pt 2 - F to C
# def F2C(f):
#     return (f - 32) * 5/9
# print(F2C(212))
# print(F2C(32))