''' Python Classes '''

from typing import List, Tuple


class SemesterRecord():
    ''' class for saving data of a student in a semester '''
    
    def get_avg(self) -> float:
        ''' returns the GPA of the current semester '''
        
        hours: int = self.get_hours()
        sum: float = 0.0
        
        
        for course_id in self.marks.keys():
            sum += self.marks[course_id][1] * self.marks[course_id][0]
            
        if hours == 0:
            return 0
            
        return sum / hours
    
    def get_hours(self) -> int:
        ''' returns the GPA of the current semester '''
        
        hours: int = 0
        
        for course_id in self.marks.keys():
            hours += self.marks[course_id][0]
            
        return hours
    
    def get_marks(self) -> List[float]:
        
        marks = []
        
        for course_id in self.marks.keys():
            marks.append(self.marks[course_id][1])
            
        return marks
    
    def __init__(self, year_sem: str, courses_dict: dict[str, Tuple[int, float]]) -> None:
        
        self.year_sem = year_sem
        self.marks = courses_dict

class Student():
    ''' Student Class '''
    
    def get_gpa(self) -> float:
        ''' calculate gpa '''
        
        sem_points = 0
        
        for sem in self.semesters.values():
            sem_points += sem.get_hours() * sem.get_avg()
            
        hours = self.get_hours()
        if hours==0:
            return 0
        
            
        return sem_points / hours
    
    def get_marks_list(self) -> List[float]:
        
        marks = []
        
        for sem in self.semesters.values():
            marks.extend(sem.get_marks())
            
        return marks
        
    
    def get_hours(self) -> int:
        ''' sum of hours '''
        
        overall_hours: int = 0
        
        for sem in self.semesters.values():
            overall_hours += sem.get_hours()
            
        return overall_hours
    
    def print_statistics(self) -> None:
        
        
        from plan import plan
        
        finished_courses = [] 
        
        for sem in self.semesters.values():
            finished_courses.extend(sem.marks.keys())
            print("Average of semester [" + str(sem.year_sem) + "] is " + str(sem.get_avg()))
        
        print("\nAnd overall average is " + str(self.get_gpa()))
        
        print("\nFinished Courses > ")
        print(finished_courses)
        
        remainings = [c for c in plan if c not in finished_courses]
        print("\nRemaining Courses > ")
        print(remainings)
        
        
            
    
    def __init__(self, id: int, semesters: dict[str, SemesterRecord]) -> None:
        
        self.id = id
        self.semesters = semesters
        
    def __str__(self) -> str:
        return "[ID:" + str(self.id) + ", gpa:" + str(self.get_gpa()) + ", hours:" + str(self.get_hours()) + ", semesters: " + str(self.semesters) + " ]"
        
    @staticmethod
    def is_valid_id(id_str) -> int:
        
        id = None
        
        try:
            id = int(id_str)
        except ValueError:
            return None
        
        if id > 110000 or id < 1260000:
            return id
        
        return None
    
    def cmp(self, term, comparator, value) -> bool:
        
        insider_value = self.get_gpa()
        
        if term == 2: # hours
            insider_value = self.get_hours()
            
        if comparator == 0:
            return insider_value == value
        elif comparator == 1:
            return insider_value < value
        else:
            return insider_value > value
        
            
        
    
            