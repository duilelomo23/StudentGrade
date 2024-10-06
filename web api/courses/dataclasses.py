from dataclasses import dataclass
from typing import Optional, List
from datetime import date



#判斷sql傳入型別
@dataclass
class CreateCourse:
    course_name: str
    teacher: str
    


    
@dataclass
class UpdateCourse:
    course_name: str
    new_course_name: str
    new_teacher: str

@dataclass
class DeleteCourse:
    course_name: str

