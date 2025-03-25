def convert_to_unreadable(s):
    result = []
    for c in s:
        if c.islower():
            result.append(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
        elif c.isupper():
            result.append(chr((ord(c) - ord('A') + 1) % 26 + ord('A')))
        else:
            result.append(c)
    return ''.join(result)

# Input
s = input("Enter a string: ")

# Output
print(convert_to_unreadable(s))
