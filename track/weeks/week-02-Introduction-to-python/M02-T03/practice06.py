sentence = input()

clean_sentence = sentence.strip()
lower_sentence = clean_sentence.lower()

normal_sentence = lower_sentence.replace('.', "")
split_sentence = normal_sentence.split()

join_sentence = "-".join(split_sentence)
upper_sentence = normal_sentence.upper()

search_result = normal_sentence.find("python")

print(f"Cleaned: {clean_sentence}")
print(f"Normalized: {normal_sentence}")
print(f"Words: {split_sentence}")
print(f"Slug: {join_sentence}")
print(f"Uppercase: {upper_sentence}")
print(f"Python Position: {search_result}")
