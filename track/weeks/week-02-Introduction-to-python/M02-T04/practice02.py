# Convert a number sign checker into function

def check_sign(number):
    if number > 0:
        value = "Positive"
    elif number < 0:
        value = "Negative"
    else:
        value = "Zero"
    return value

number = int(input())
result = check_sign(number)
print(result)
