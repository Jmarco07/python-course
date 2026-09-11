import random
import my_module

random_integer = random.randint(1, 10)
random_number_with_floating_point = random.random()
random_float_with_range = random.uniform(1, 10)
print("My favorite number is: ", my_module.my_favorite_number)

print("Random number between 1 - 10: ", random_integer)

print("Random number with floating point: ", random_number_with_floating_point)

print("Random number with floating point between 1 -10: ", random_float_with_range)