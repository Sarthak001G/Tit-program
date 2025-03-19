# Read the number of test cases
T = int(input("Enter number of test cases: "))

for _ in range(T):
    # Read the size of the series
    N = int(input("Enter the size of the series: "))
    
    # Read the series of numbers
    numbers = list(map(int, input("Enter the numbers: ").split()))

    # Find and print the minimum and maximum values
    print("Minimum:", min(numbers), "Maximum:", max(numbers))
