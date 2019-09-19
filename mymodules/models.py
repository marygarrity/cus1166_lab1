#Returns a Student object with the given name and grade
class Student(object):
    #Initialize:
    def __init__(self, student_name, student_grade):
        self.student_name = student_name
        self.student_grade = student_grade

    #set_grade(grade)
    #(sets grade of student)
    def set_grade(self,grade):
        self.student_grade = grade

    #get_grade
    #(returns grade of student)
    def get_grade(self):
        return self.student_grade

    #print_student_info
    #(print name and grade of student in formated string)
    def print_student_info(self):
        print("Student Name:  " + str(self.student_name) + "     Grade:  " + str(self.student_grade)) #how to format?
