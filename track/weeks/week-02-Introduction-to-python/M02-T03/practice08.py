skills = []
for i in range(5):
    skill = input()
    skills.append(skill)

skill_record = tuple(skills)

print(f"Skill Record: {skill_record}")
print(f"First Three: {skill_record[:3]}")
print(f"Last Two: {skill_record[-2:]}")
print(f"Alternate Skills: {skill_record[::2]}")
print(f"Reversed Skills: {skill_record[::-1]}")
