n = int(input())
scores = []

for i in range(n):
    score = int(input())
    scores.append(score)

search_score = int(input())

highest = max(scores)
lowest = min(scores)
total = sum(scores)

print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Total Score: {total}")

status = "Not Found"
for i in scores:
    if i == search_score:
        status = "Found"

print(f"Search Result: {status}")
