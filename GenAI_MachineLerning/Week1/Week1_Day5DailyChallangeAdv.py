import random

# Generate list of random numbers
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728

# Use a set to store numbers we've already seen
seen_numbers = set()

# Store found pairs
pairs = set()

# Find pairs
for number in list_of_numbers:
    complement = target_number - number

    # Check if complement already exists
    if complement in seen_numbers:
        # Sort pair so duplicates like (1000,2728) and (2728,1000) are avoided
        pair = tuple(sorted((number, complement)))
        pairs.add(pair)

    seen_numbers.add(number)

# Print results
print(f"Pairs that sum to {target_number}:\n")

for a, b in pairs:
    print(f"{a} and {b} sum to {target_number}")