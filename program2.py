
numbers = []

print("Enter 5 numbers:")

for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

greatest = max(numbers)


print("Given numbers:", numbers)
print("Greatest number is:", greatest)