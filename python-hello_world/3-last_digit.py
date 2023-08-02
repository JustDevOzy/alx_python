import random
number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
suffix = ''

if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    suffix = "and is greater than 5"
elif last_digit == 0:
    suffix = "and is 0"
else:
    suffix = "and is less than 6 and not 0"


print("Last digit of" , number , "is", last_digit, suffix)