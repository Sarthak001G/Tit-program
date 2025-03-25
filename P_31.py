def fahrenheit_to_celsius(start, end, step):
    print("Fahrenheit_value  equivalent_celsius_value")
    for f in range(start, end + 1, step):
        c = int((f - 32) * 5 / 9)
        print(f"{f} {c}")

# Input in one line
start, end, step = map(int, input("Enter start, end, and step size separated by spaces: ").split())

# Output
fahrenheit_to_celsius(start, end, step)
