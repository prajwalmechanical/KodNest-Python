class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profile = []

    def add_student_profile(self, student):
        self.student_profile.append(student)

    def filter_students_by_course(self, search_course):
        matching_course = []

        for student in self.student_profile:
            if student.course.lower() == search_course.lower():
                matching_course.append(student)

        return matching_course


manager = PlacementManager()
n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()
    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

search_course = input().strip()
result = manager.filter_students_by_course(search_course)

if result:
    for student in result:
        print(student)
else:
    print(f"No students found for course: {search_course}")
