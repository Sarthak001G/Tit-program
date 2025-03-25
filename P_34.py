l = list(map(int, input("Enter numbers separated by space: ").split()))
a = -1
b=-2


for i in range(len(l)):
    if l[i] > a:
        a = l[i]

for i in range(len(l)):
    if l[i]>b and b!=l:
        b = l[i]


print("List:", l)
print("Maximum number:", a,b)
