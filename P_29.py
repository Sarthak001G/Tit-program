def alternate_case(s):
    result = []
    upper = True

    for char in s:
        if char.isalpha():
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper
        else:
            result.append(char)

    return ''.join(result)

# Input
s = input("Enter a string: ")

# Output
print("Alternating Case: ", alternate_case(s))
