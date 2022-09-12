##This is some code for Lecture 11 PyCh8 on working with files.

# One Example we used in class.  Note that you will need to change the directory.
haha = open("PyCh8-ENGRJokes.txt", "r", encoding='utf-8')
for line in haha:
    print(line)
haha.close()

# # Extra practice
# # Below, work to either write or append the txt file, or print various lines or sections of the txt file. 