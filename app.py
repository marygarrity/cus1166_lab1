"""
Your app.py file must use the Student class, and the
average_grade method you defined the mymodules module.
"""
from mymodules.models import Student
from mymodules.math_utils import average_grade
import random #for generating random numbers

def main():
    #Hardcode roster:
    #roster = ["Anna", "Tom", "John", "Sam", "Alex", "Emma", "Jack", "Jane", "Mark", "Chris"]
    #Dictionary:
    #grades = {"Anna" : 100, "Tom" : 90, "John" : 97, "Sam" : 95, "Alex" : 82, "Emma" : 93, "Jack" : 89, "Jane" : 100, "Mark": 80, "Chris" : 75}

    #Create a roster of 10 students:
    roster = []
    names = ["Anna", "Tom", "John", "Sam", "Alex", "Emma", "Jack", "Jane", "Mark", "Chris"]

    for i in range(10):
        name = str(names[i])
        grade = random.randint(60, 100) #grade is random number 60-100
        #change variable names?
        student = Student(name, grade) #inside for loop!
        roster.append(student) #inside for loop!

    #Print the list of students:
    for student in roster:
        student.print_student_info();

    #Print the average score of the current roster:
    print("Average grade: " + str(average_grade(roster))) #outside for loop!
main() #ends main and runs it, same indetation as def main():
