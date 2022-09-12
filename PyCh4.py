# Part 1.  Add comments to each block of code 
# to help understand what is happening
empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

# [What happens below here? Replace me!]
if empty_list == []:
    print("It's an empty list!")

# [What happens below here? Replace me!]
if empty_tuple:
    print("It's not an empty tuple!")

# [What happens below here? Replace me!]
if not empty_string:
    print("This is an empty string!")

# [What happens below here? Replace me!]
if not nothing:
    print("Then it's nothing!")

# # Uncomment me by highlighting lines 24 - 33 and
# # pressing ctrl + k + u.  Ctrl + k + c autocomments
# x = None

# if x:
#   print("Do you think None is True?")
# elif x is False:
#   print ("Do you think None is False?")
# else:
#   print("None is not True, or False, None is just None...")

#print('a' + 'x' if '123'.isdigit() else 'y' + 'b')
#print('a' + ('x' if '123'.isdigit() else 'y') + 'b')

#Final coding task start
school_prep_feeling = 5
if school_prep_feeling > 7:
    print('Feel free to skip out on the school work tonight')
else:
    print('You need to work on school!')
