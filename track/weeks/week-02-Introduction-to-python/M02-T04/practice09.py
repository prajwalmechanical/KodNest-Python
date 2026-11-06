# Count word frequencies using a dictionary

n = int(input())

word_frequency = {}

for _ in range(n):
    word = input().strip()
    word_frequency[word] = word_frequency.get(word, 0) + 1

for word, count in word_frequency.items():
    print(word, count)
