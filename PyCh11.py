# CHEE 205 Lecture 14 - PyCh11 - Classes begins with the creation 
# of the class dog.  Below is the code for creating the class and 
# adding four dog objects.  Add commencts to this code to help 
# you understand what each line does!

class dog():
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def bark(self):
        print("%s just barked!!!" % self.name)

    def sleep(self):
        print("%s just slowly closed their eyes, rolled up into a ball of fur, and fell asleep" % self.name)

    def eat(self):
        print("%s just at their food in record speed!!!" % self.name)

    def identify(self):
        print("%s, the best dog ever, is a %s, is %s years old, and is the color of %s" % (self.name, self.breed, self.age, self.color))

#Creation of Frank, the beloved
dog1 = dog("Frank", "Pit Bull", 14, "rust")
dog1.bark()
dog1.sleep()
dog1.eat()
dog1.identify()

#Creation of Margaret Luise Ross Sumner Hempel
dog2 = dog("Margaret Luise Ross Sumner Hempel", "Golden Retriever", "dead", "heaven on earth")
dog2.bark()
dog2.sleep()
dog2.eat()
dog2.identify()

# #Creation of Doober Dog
# dog3 = dog("Doober Dog", "Golden Retriever", "dead", "Wheat ready to be harvested")
# dog3.bark()
# dog3.sleep()
# dog3.eat()
# dog3.identify()

# #Creation of Flucifer
# dog4 = dog("Flucifer", "Pomeranian", "too many", "everlasting terror on the world")
# dog4.bark()
# dog4.sleep()
# dog4.eat()
# dog4.identify()

# # Creating the Student Class
# class UofA_student():
#     def __init__(self, name, gpa, age, school_prep):
#         self.name = name
#         self.gpa = gpa
#         self.age = age
#         self.school_prep = school_prep #on a scale from 1 to 10.

#     def socialize(self):
#         print("%s just effectively communicated with their friend!!!" % self.name)

#     def sleep(self):
#         print("%s fell asleep in class and was noted by their classmates.  Oops." % self.name)

#     def eat(self):
#         print("%s just at their food and is now ready to study!!!" % self.name)

#     def study(self):
#         try:
#             if self.gpa >= 3.0:
#                 print("Yay this student is doing well enough to graduate!")
#             elif self.gpa >= 2.0 and self.gpa < 3.0:
#                 print("This student should probably be working harder!")
#             elif self.gpa <= 2.0:
#                 print("This student needs to see Lori ASAP")
#         except:
#             print("You need to put the gpa in as a number between 0 and 4!")
#         try:
#             if self.school_prep > 8.0:
#                 print("Yay %s can probably chill and do well on the next exam" % self.name)
#             elif self.school_prep >= 5.0 and self.school_prep <= 8.0:
#                 print("%s should probably study!" % self.name)
#             elif self.gpa <= 2.0:
#                 print("%s really should study ASAP" % self.name)
#         except:
#             print("You need to put the feeling or prep in as a number between 1 and 10!")

# student1 = UofA_student("Theodor Oliver Rosevelt III", 2.6, 21, 6)
# student1.study()

# # MC3 - test
# class test:
#      def __init__(self,a="Hello World"):
#          self.a=a
 
#      def display(self):
#          print(self.a)
# obj=test()
# obj.display()

# # MC6 - change
# class change:
#     def __init__(self, x, y, z):
#         self.a = x + y + z
 
# x = change(1,2,3)
# y = getattr(x, 'a')
# setattr(x, 'a', y+1)
# print(x.a)

# # MC7 - test
# class test2:
#      def __init__(self,a):
#          self.a=a
 
#      def display(self):
#          print(self.a)
# try:
#     obj=test2()
#     obj.display()
# except:
#     print("missing 1 required positional arguement: 'a'")

# # MC8 - A
# class A:
# 	def __init__(self,b):
# 		self.b=b
# 	def display(self):
# 		print(self.b)
# obj=A("Hello")
# del obj

# # MC9 - test3
# class test3:
#     def __init__(self):
#         self.variable = 'Old'
#         self.Change(self.variable)
#     def Change(self, var):
#         var = 'New'
# obj=test3()
# print(obj.variable)

# # MC11 - fruits
# class fruits:
#     def __init__(self, price):
#         self.price = price
# obj=fruits(50)
# obj.quantity=10
# obj.bags=2
# print(obj.quantity*obj.price*obj.bags)

# # MC12 - demo
# class Demo:
#     def __init__(self):
#         pass
#     def test(self):
#         print(__name__)
 
# obj = Demo()
# obj.test()
