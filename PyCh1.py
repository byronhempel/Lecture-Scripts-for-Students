msg = "hello world"
print(msg)

num1 = 20 #variable for number 1
num2 = 45 #variable for number 2
num_sum = num1 + num2 #adds num1 to num2
num_diff = num1 - num2 #finds difference
num_prod = num1 * num2 #finds product
num_quot = num1 / num2 #finds quotient
#below is the bonus display.  It uses a variable
#substitution to display numbers in a string
print('The sum is %s, the difference is %s, \
the product is %s, the quotient is %s.' % \
(num_sum, num_diff, num_prod, num_quot))

import random #pulls in the library random
rand_num = random.randrange(0,10,2) #creates a
#random integer from 0 to 10
print(rand_num) #prints the number created

#prints three random integers from 0 to 10
print(random.randrange(0,10,2))
print(random.randrange(0,10,2))
print(random.randrange(0,10,2))