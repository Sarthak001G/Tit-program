def is_power_of_two(n):
    if n < 1:
        return 0
    while n > 1:
        if n % 2 != 0:
            return 0
        n //= 2
    return 1

# Taking input from user
n = int(input())
print(is_power_of_two(n))

