import random
number = random.randint(-100, 100)



if number > 0:
    result = "is positive"

elif number == 0:
    result = "is zero"

else:
    result = "is negative"


print(f"The number {number}: {result}")
