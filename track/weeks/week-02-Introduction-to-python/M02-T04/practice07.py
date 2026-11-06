# Build a Reusable student eligibility Checker

def check_eligibility(marks, attendance, project_completed):
    if marks >= 60:
        if attendance >= 75:
            if project_completed == "yes":
                return "Eligible"

    return "Not Eligible"

marks = int(input())
attendance = int(input())
project_completed = input().strip().lower()

result = check_eligibility(marks, attendance, project_completed)
print(result)
