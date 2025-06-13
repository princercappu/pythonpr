def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

numbers = [float(input("Enter a number: ")) for _ in range(5)]
target = float(input("Enter the target number: "))

result = linear_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
