def alternate_case(s):
    result = []

    for i in range(len(s)):
        if i % 2 == 0:  # Even index (0-based, first character is uppercase)
            result.append(s[i].upper())
        else:  # Odd index
            result.append(s[i].lower())
    
    return ''.join(result)

# Input
s = input("Enter a string: ")
print("Alternating case string:", alternate_case(s))
