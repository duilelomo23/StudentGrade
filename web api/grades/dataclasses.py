from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class Creategrade:
    student_name: str
    course_name: str
    grade: int
@dataclass
class Updategrade:
    student_name: str
    course_name: str
    grade: int


@dataclass
class Deletegrade:
    student_name: str
    course_name: str
