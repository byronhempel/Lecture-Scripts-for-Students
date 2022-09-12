# # Seeing what functions math has
# import math
# print(dir(math))

# for importing packages, there are two main methods.  If you download Anaconda,
# you get a recommendation to install Jupyter Notebook.  This is a collaborative tool
# that you are welcome to use in the class to share Python code. See here for more info:
# https://www.anaconda.com/products/distribution/download-success-2

# You are also welcome to go the pip route for installing Python pakcages:
# https://realpython.com/what-is-pip/.  This is how I downloaded my packages. 
# The website: https://packaging.python.org/en/latest/tutorials/installing-packages/ 
# guides you through this process.  Note that when you reach the section on "installing
# from PyPi", for windows, you will run: 

# py -m pip install numpy

# to install numpy.  Repeat the process for the other packages.

# Run the following.  Work to get each module imported so you can see the directory 
# of functions available to you.  You will not need to memorize these; it is a good
# way to check to see if you have the package downloaded successfully.
import math
print(dir(math))
import numpy
print(dir(numpy))
import matplotlib
print(dir(matplotlib))
import scipy
print(dir(scipy))
import pandas
print(dir(pandas))

# When this runs successfully, congratulations!  You can now use any of these packages
# and you now know how to run different packages in Python (through Visual Studio Code)! 