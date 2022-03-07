from utils import read_files, add_semester, add_new_record, is_number, update_mark, student_statistics, global_statistics, search

##########################################

def admin():
    
    while(True):
    
        print("""\n 
|===================|
  \t Menu
|===================|\n
1- Add New Record.
2- Add new semester with student course and grades
3- Update
4- Student statistics
5- Global statistics
6- Searching
7- Exit\n
Enter Command Number: 
            """)
        
        cmd = is_number(input())
        if cmd == 1:
            
            try:
                add_new_record()
            except KeyError:
                print("\nID is not unique")
        elif cmd == 2:
            try:
                add_semester()
            except KeyError:
                print("\nID not found")
        elif cmd == 3:
            try:
                update_mark()
            except KeyError:
                print("\nID not found")
        elif cmd == 4:
            try:
                student_statistics()
            except KeyError:
                print("\nID not found")
        elif cmd == 5:
            global_statistics()
        elif cmd == 6:
            search()
        else:
            break
        

def student():
    
    while(True):
    
        print("""\n 
|===================|
  \t Menu
|===================|\n
1- Student statistics
2- Global statistics
7- Exit\n
Enter Command Number: 
            """)
        
        cmd = is_number(input())
        if cmd == 1:
            try:
                student_statistics()
            except KeyError:
                print("\nID not found")
        elif cmd == 2:
            global_statistics()
        else:
            break

##########################################

user_type = int(input("\n\nEnter 1 for admin login, 2 for student: "))

read_files()

if user_type == 1:
    admin()
else:
    student()
