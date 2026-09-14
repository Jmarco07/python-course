numbers = [3,45,34,2,46,654,4,6,7,32,1,9,4,2,3]

print(f"Unsorted numbers: {numbers}")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            print(f"Swapped {numbers[j]} and {numbers[i]}")

print(f"Sorted numbers: {numbers}")