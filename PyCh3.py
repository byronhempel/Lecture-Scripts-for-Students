L = [] 
print(dir(L))

T = () 
print(dir(T))

d = {} 
print(dir(d))

#Students Dictionaries in a List
student1 = {'age': 27, 'name': 'Jack'} #student 1 created
student2 = {'age': 30, 'name': 'Mel'} #student 2 created
all_students = [student1, student2] #list of students
print(all_students) #displaying the students

student3 = {'age': 21, 'name': 'Lu'} #student 3 created
student4 = {'age': 18, 'name': 'Ahmad'} #student 4 created
all_students.append(student3) #adds student 3 to the master list
all_students.append(student4) #adds student 4 to the master list
print(all_students) #displays the students