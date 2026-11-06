class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.students = []

    def add_student_profile(self, student):
        self.students.append(student)

    def display_student_profiles(self):
        if not self.students:
            print("No student profiles available")
        else:
            for student in self.students:
                print(student)


manager = PlacementManager()
n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

manager.display_student_profiles()
