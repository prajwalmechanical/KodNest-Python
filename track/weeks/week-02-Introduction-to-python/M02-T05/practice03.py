class StudentProfile:
    def __init__(self, student_id, name, course, score, is_placed):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        placement = "Placed" if self.is_placed else "Not Placed"
        return f"""STUDENT PROFILE
ID: {self.student_id}
Name: {self.name}
Course: {self.course}
Score: {self.score}
Placement Status: {placement}"""

student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip().lower()

is_placed = placement_input == "yes"

student = StudentProfile(student_id, name, course, score, is_placed)
print(student)
