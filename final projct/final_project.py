import random
from turtle import update
from task1 import Course
from task1 import Studant

studants_list = []
courses_list = []

def removeandedit_studant (studant_id,studants_list):
                index = 0
                for i in studants_list:
                    if i["studant_id"] in studant_id:
                        return index
                return -1

def find_studant (studant_name,studants_list):
                index = 0
                for i in studants_list:
                    if i["studant_name"] in studant_name:
                        return index
                return -1
def find_course (course_name,courses_list):
                index = 0
                for i in courses_list:
                    if i["course_name"] in course_name:
                        return index
                return -1


while True:
    x = int(input("1:Add New Studant.\t\t2:Remove Student.\t\t3:Edit Studant\n\
4:Display All Studant. \t\t5:Create New Course.\t\t6:Add Course to Studant\n\
7:Exit.\n"))
    if x == 1:
            studant_id = str(random.randint(1, 10))
            studant_name = input("inter the studant name :")
            studant_course=[]
            studant_class = None
            while True:
                studant_class = input("choose A or B or C \n")
                if studant_class in ["A", "B" , "C"]:
                    break
            studant = Studant (studant_name,studant_id,studant_class,studant_course)  
            studants_list .append (
                 {  "studant_name" : studant_name,
                    "studant_id" : studant_id,
                    "studant_class" : studant_class,
                    "studant_course" : studant_course}
)
            print("Studunt save successfully")      


    elif x == 2:
         studant_id = str(input("Enter studunt id: "))
         studant_index = removeandedit_studant(studant_id , studants_list)
         if studant_index == -1:
                    print("Studunt Not Exist")
         else:
                    
            for i in range(len(studants_list)):
                    if studants_list[i]['studant_id'] == studant_id:
                       del studants_list[i]
                       break
            # print("aftar list :" + str(studants_list))  


    elif x == 3:
         studant_id = str(input("Enter studunt id: "))
         studant_index = removeandedit_studant(studant_id , studants_list) 
         if studant_index == -1:
             print("Studunt Not Exist")
        
         else:
            newstudant_name = str(input("entur new name:"))
            while True:
                newstudant_class = input("entur new name A or B or C \n")
                if studant_class in ["A", "B" , "C"]:
                    break
           
         for i in studants_list:
                    if i['studant_id'] == studant_id: 
                        i['studant_name'] = newstudant_name
                        i['studant_class'] = newstudant_class
                          
        #  print("aftar list :" + str(studants_list)) 



    elif x == 4:
        print("student name:\t\t" , "studant class:\t\t", "studant courses:\t\t","studant id" )
        for i in studants_list:
            print(i["studant_name"] , "\t\t\t" ,i['studant_class'] , "\t\t\t" ,i['studant_course'], "\t\t" ,i['studant_id'] )  


              
    elif x == 5:
        course_name = input("inter the course name :")
        course_class = None


        while True:
            course_class = input("choose A or B or C \n")
            if course_class in ["A", "B" , "C"]:
                break
        course = Course (course_name,course_class)  
        courses_list .append (
            {
                "course_name" : course_name,
                "course_class" : course_class
        
                
            })
        # print("list:" + str(courses_list))


    elif x == 6:
        studant_name = input("enter student name")
        studant_index = find_studant(studant_name , studants_list)
        if studant_index == -1:
            print("studant Not Exist")
        else:
            course_name = input("enter course name")
            course_index = find_course(course_name , courses_list)
            if course_index == -1:
                print("Course Not Exist")
            else:
                for i in studants_list:
                    if i['studant_name'] == studant_name:
                        st = i['studant_class']
                for i in courses_list:
                    if i['course_name'] == course_name:
                        co = i['course_class']
        if st == co :
            for i in studants_list:
                    if i['studant_name'] == studant_name: 
                       i['studant_course'] += [course_name]
                    
        else:
                    print("The student and the course are not of the same class")

    elif x == 7:
        exit()



