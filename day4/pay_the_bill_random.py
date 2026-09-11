import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(f"The selected friend is: {random.choice(friends)}")

# Option 2
random_index = random.randint(0, len(friends) - 1)

print(f"The selected friend is: {friends[random_index]}")

