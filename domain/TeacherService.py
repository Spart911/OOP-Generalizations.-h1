from domain.person import Person
from domain.teacher import Teacher
from typing import List

class iPersonService:
    def add_person(self, person: Person):
        pass

    def remove_person(self, person: Person):
        pass

    def get_all_persons(self) -> List[Person]:
        pass

class PersonComparator:
    def __call__(self, person1: Person, person2: Person) -> int:
        return person1.age - person2.age

class TeacherService(iPersonService):
    def __init__(self):
        self.teachers = []

    def add_person(self, teacher: Teacher):
        self.teachers.append(teacher)

    def remove_person(self, teacher: Teacher):
        self.teachers.remove(teacher)

    def get_all_persons(self) -> List[Teacher]:
        return self.teachers

    def get_sorted_teachers(self) -> List[Teacher]:
        return sorted(self.teachers, key=PersonComparator())

teacher_service = TeacherService()
sorted_teachers = teacher_service.get_sorted_teachers()
for teacher in sorted_teachers:
    print(teacher)
