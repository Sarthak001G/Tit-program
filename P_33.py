def replace_repeating_characters(s):
    seen = set()
    result = []

    for c in s:
        if c != ' ' and c in seen:
            result.append('-')
        else:
            result.append(c)
            seen.add(c)

    return ''.join(result)

# Input
s = input("Enter a sentence: ")

# Output
print(replace_repeating_characters(s))
