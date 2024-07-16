# Write program that repeatedly asks from user no until string 'done' is typed.The program should print sum  of all  numebr entered.
total = 0
s = input ('Enter a Numberor "done":')
while s !='done':
    num = int (s)
    total = total + num
    s = input ('Enter a Number or "done"')
print('The sum of entered number is', total)
