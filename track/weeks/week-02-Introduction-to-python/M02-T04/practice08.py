# Count unique student registrations

n = int(input())

registrations = set()

for _ in range(n):
    student_id = input().strip()
    registrations.add(student_id)

search_id = input().strip()

unique_count = len(registrations)
duplicate_count = n - len(registrations)

print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")
