import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
comparison = " "



if last_digit > 5 :
    comparison = "and is greater than 5"

elif last_digit == 0 :
    comparison = "and is zero"

else:
    comparison ="and is less than 6 and not zero"

print(f"Last digit of {number} is {last_digit}, {comparison} ")