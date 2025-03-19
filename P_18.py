N = int(input())


def digital_root(num):
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10  # Get the last digit
            num //= 10  # Remove the last digit
        num = digit_sum
    return num
