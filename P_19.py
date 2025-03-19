def encrypt(s):
    encrypted_message = []
    
    for i in range(len(s)):
        if (i + 1) % 2 == 1:  # Odd position (1-based)
            encrypted_message.append(chr(ord(s[i]) - 2))
        else:  # Even position (1-based)
            encrypted_message.append(chr(ord(s[i]) + 2))
    
    return ''.join(encrypted_message)

# Input
s = input("Enter a string: ")
print("Encrypted string:", encrypt(s))



print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97



print(chr(65))  # Output: A
print(chr(97))  # Output: a
