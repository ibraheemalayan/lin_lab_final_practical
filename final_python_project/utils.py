
from os import path
from models import Student, SemesterRecord
from typing import Dict, List

students: Dict[int, Student] = {}

def path_id(id: int):
    return path.join("db", str(id) + ".txt")

def get_hours_from_course_id(course_id) -> int:
    
    return int(course_id[5])

def read_file(id: int) -> Student:
    
    print("\n\n")
    
    semesters = {}
        
    with open( path_id(id) , "r") as f:
        
        print(f"File: {id}")
        
        file_data = f.read()
        
        if len(file_data) < 2:
            print("File is empty")
            return
            
        import json
        
        try:
            d = json.loads(file_data)
            print("File is JSON (Dict in Dict)")
            return
        except json.JSONDecodeError as exc:
            print("Not in json format")
            
        
        
        try:
            for line in file_data.split('\n'):
                
                year_sem = line.split(";")[0].strip()
                
                recs = line.split(";")[1].split(",")
                
                sem_dict = {}
                
                
                for r in recs:
                    splitted = r.strip().split(" ")
                    
                    course_id = splitted[0]
                    mark = float(splitted[1])
                    
                    hours = get_hours_from_course_id(course_id)
                    
                    sem_dict[course_id] = (hours, mark)
                    
                semesters[year_sem] = SemesterRecord(year_sem=year_sem, courses_dict=sem_dict)
                print("File is CSV")
                return
        except IndexError as e:
            print("Not in CSV format")
            
        # check if yaml
        import yaml
        
        try:
            d = yaml.safe_load(f)
            print("File is YAML (Dict in Dict)")
            return
        except yaml.YAMLError as exc:
            print("Not a dictionary in dictionary format")
           
    return Student(id, semesters=semesters)
    
def write_student(std: Student):
    ''' update student file '''
    
    with open( path_id(std.id) , "w") as f:
        for sem in std.semesters.keys():
            
            line = sem + " ; "
            
            for c_id in std.semesters[sem].marks.keys():
                line += c_id + " " + str(std.semesters[sem].marks[c_id][1]) + ","
                
            f.write(line[:-1] + "\n")

def read_files():

    from os import walk, path

    filenames = next(walk("db"), (None, None, []))[2]
    
    for filename in filenames:
        
        id = Student.is_valid_id(filename.split(".")[0])
        
        if id is None:
            continue
        
        students[id] = read_file(id)
        
        
        
    # for st in students:
    #     print(st)
        
def is_number(s):
    
    try:
        return int(s)
    except ValueError:
        return None
    
####  ####  ####  ####  ####  ####  ####  ####  ####  
################## Admin Commands ##################
####  ####  ####  ####  ####  ####  ####  ####  ####  

# 1
def add_new_record():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id in students:
        raise KeyError("ID is not unique")
    
    students[id] = Student(id, {})
    
    write_student(students[id])
    
    
# 2
def add_semester():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id not in students:
        raise KeyError("Student with this ID was not found")
    
    year_sem = input("Enter Year/Semester: ")
    
    print("How many courses were completed in this semester : ")
    count = is_number(input())
    
    if not count or count < 1:
        print("! invalid input")
        return
    
    sem_dict = {}
    
    for i in range(count):
        
        course_id = input("Enter Course ID:").strip()
        
        if not course_id or len(course_id) < 7 or (course_id[:4] != "ENEE" and course_id[:4] != "ENCS") :
            print("! invalid input")
            return
        
        mark = is_number(input("Enter Mark:"))
        
        if not mark:
            print("! invalid input")
            return
        
        hours = get_hours_from_course_id(course_id)
        
        sem_dict[course_id] = (mark, hours)
        
    students[id].semesters[year_sem] = SemesterRecord(year_sem=year_sem, courses_dict=sem_dict)
    
    write_student(students[id])
    
    
# 3
def update_mark():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id not in students:
        raise KeyError("Student with this ID was not found")
    
    course_id = input("Enter Course ID:").strip()
        
    if not course_id or len(course_id) < 7 or (course_id[:4] != "ENEE" and course_id[:4] != "ENCS") :
        print("! invalid input")
        return
    
    for sem in students[id].semesters.values():
        
        if course_id in sem.marks:
            
            mark = is_number(input("Enter Mark:"))
        
            if not mark:
                print("! invalid input")
                return
            
            sem.marks[course_id] = (sem.marks[course_id][0], mark)
            write_student(students[id])
            return
        
    print("Course not found")
    
# 4
def student_statistics():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id not in students:
        raise KeyError("Student with this ID was not found")
    
    students[id].print_statistics()
    
# 5
def global_statistics():
    
    sum = 0
    hours_sum = 0
    sems_count = 0
    
    marks = []
    
    for st in students.values():
        
        marks.extend(st.get_marks_list())
        
        sum += st.get_gpa()
        
        for sem in st.semesters.values():
            hours_sum += sem.get_hours()
            sems_count += 1
            
    print("Avg > " + str( sum/len(students)))
    print("Hours Per Sem Avg >> " + str( hours_sum/sems_count))
    
    import matplotlib.pyplot as plt
    
    plt.hist(marks)
    plt.show()
    
# 6
def search():
    
    print("\nChoose the search term:\n\t1-Avg\n\t2-hours")
    
    t = is_number(input("\nEnter Term Number:"))
    
    print("\nChoose the condition:\n\t0-equal\n\t1-less than\n\t2-greater than")
    
    c = is_number(input("\nEnter condition number: "))
    
    val = is_number(input("\nEnter value to compare with: "))
    
    for s in students.values():
        if s.cmp(term=t, comparator=c, value=val):
            print(s.id)
    
    
    
    