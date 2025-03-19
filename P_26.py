def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_twisted_prime(n):
    if not is_prime(n):
        print(f"{n} is not a Twisted Prime")
        return
    
    # Reverse the number
    reversed_n = int(str(n)[::-1])

    # Check if reversed number is also prime
    if is_prime(reversed_n):
        print(f"{n} is a Twisted Prime")
    else:
        print(f"{n} is not a Twisted Prime")

# Input
n = int(input("Enter a number: "))
is_twisted_prime(n)

