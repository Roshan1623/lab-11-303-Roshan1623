def in_order(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return False
    return True

numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

if in_order(numbers):
    print("In descending order")
else:
    print("Not in order")
