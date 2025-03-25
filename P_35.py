l = list(map(int, input("Enter numbers separated by space: ").split()))

# Initialize variables
largest = second_largest = float('-inf')

# Find the largest and second largest
for num in l:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("No second largest number.")
else:
    print("List:", l)
    print("Second largest number:", second_largest)
