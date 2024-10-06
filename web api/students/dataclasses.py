from dataclasses import dataclass
from typing import Optional, List
from datetime import date




@dataclass
class CreateStudent:
    student_name: str
    student_number: int

@dataclass
class UpdateStudent:
    student_name: str
    new_student_name: str
    new_student_number: int


@dataclass
class DeleteStudent:
    student_name: str

