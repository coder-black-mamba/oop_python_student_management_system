# Bismillahir Rahmanir Rahim
import random


# this is my function for getting random number for student id
def get_random_id():
    return str(random.randint(10000, 99999))




# The main Student Database Class
class StudentDatabase:
    # add a class attribute named student_list
    __student_list = []

    def __init__(self):
        pass


    # defining add_student method to insert an object of Student Class
    @classmethod
    def add_student(cls,student_obj):
        cls.__student_list.append(student_obj)


    # defining the class method for viewing all the student data
    @classmethod
    def view_all_students(cls):
        if len(cls.__student_list)>0:
            for student in cls.__student_list:
                student.view_student_info(db_style=True)
                # Bad Practise - churi kora style
                # print(f"Student ID: {student._Student__student_id}, Name : {student._Student__name}, Department : {student._Student__department}, Enrollment Status : {student._Student__is_enrolled}")
        else:
            print("No Student Data Found in the Database :)")

    @classmethod
    def find_by_id(cls, student_id):
        for student in cls.__student_list:
            if student.get_student_id() == student_id:
                return student
        return None


# defining the Student Class
class Student:
    def __init__(self, student_id, name,department,is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    # getter for student id
    def get_student_id(self):
        return self.__student_id


    # getter for student info
    def get_student_info(self):
        student_info_dict={
            "student_id":self.__student_id,
            "name":self.__name,
            "department":self.__department,
            "is_enrolled":self.__is_enrolled
        }
        return student_info_dict


    # method for enrolling student
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled=True
            print(f"Student [ ID : {self.__student_id}, Name : {self.__name}, Department : {self.__department}, Enrolled : {self.__is_enrolled} ] Enrollment Successful 🤓🤓🤓")
            # print(f"ID : {self.__student_id}, Name : {self.__name}, Department : {self.__department}, Enrolled : {self.__is_enrolled}")
        else:
            raise  Exception(f"Student [ ID: {self.__student_id} , Name : {self.__name} ] is already enrolled :) ")



    # method for drop student
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled=False
            print(f"Student [ ID : {self.__student_id}, Name : {self.__name} ] - Dropped Successfully 😭😭😭")
        else:
            raise  Exception(f"Student [ ID: {self.__student_id} , Name : {self.__name} ] is Not Enrolled :) ")




    # view student info method for viewing the student data
    def view_student_info(self ,db_style=False):
        enrollment_status="Not Enrolled"

        if self.__is_enrolled:
            enrollment_status="Enrolled"

        # for my 2 type of style
        if db_style:
            print(f"ID : {self.__student_id}, Name : {self.__name}, Department : {self.__department}, Enrolled : {enrollment_status}")
        else:
            print(f"The ID of the student {self.__name} is: {self.__student_id} .He/She is in the DEPT of {self.__department} and currently he/she is  {enrollment_status} .")



# intialization and usesof the classes
kodu = Student(get_random_id(), "Kodu", "CSE")
jodu = Student(get_random_id(), "Jodu", "CSE")
modu = Student(get_random_id(), "Modu", "EEE")
lodu = Student(get_random_id(), "Lodu", "EEE")


# kodu.enroll_student()
#
# jodu.view_student_info()
# kodu.view_student_info()
#
# kodu.drop_student()
# jodu.drop_student()
# modu.drop_student()

# StudentDatabase.view_all_students()

def input_students():
    name = input("Please Input Name : ")
    department = input("Please Input Department : ")

    if len(name) and len(department):
        new_student= Student(get_random_id(),name,department)
        # print(f"{new_student.view_student_info(db_style=True)}")

        new_student_info=new_student.get_student_info()
        print(f"Student [ {str(new_student_info)[1:-1]} ] Successfully Added :)")
        # StudentDatabase.add_student(new_student)
    else:
        print("Please Input Correct Data")
        # if student data is not valid then it will prompt use recursively
        # input_students()



# menu-driven system
while True:
    print("")
    print("============_Basic_Student_Management_System_(blackMamba)_===========")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Enroll Student")
    print("4. Drop Student")
    print("5. Exit")
    choice = input("Enter your choice (ex:1) : ")

    if choice == "1":
        StudentDatabase.view_all_students()
    elif choice=="2":
        input_students()
    elif choice == "3":
        s_id = input("Enter student ID : ")
        student = StudentDatabase.find_by_id(s_id)
        if student:
            try:
                student.enroll_student()
            except Exception as e:
                print(e)
        else:
            print(f"Student [ ID : {s_id} ] not found.")
    elif choice == "4":
         # Drop Student
        s_id = input("Enter student ID : ")
        student = StudentDatabase.find_by_id(s_id)
        if student:
            try:
                student.drop_student()
            except Exception as e:
                print(e)
        else:
            print(f"Student [ ID : {s_id} ] not found.")
    elif choice == "5":
        print("Dhonnobad Ar Asben Na  🙃")
        break
    else:
        print("Invalid choice. Please try again.")
        continue










