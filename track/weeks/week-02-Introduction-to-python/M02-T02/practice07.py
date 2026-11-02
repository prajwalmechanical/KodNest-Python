number_count = int(input())

positive_count = 0
negative_count = 0
zero_count = 0
total = 0

for i in range(number_count):
    number = int(input())
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

    total = total + number

print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zero Count: {zero_count}")
print(f"Total: {total}")
