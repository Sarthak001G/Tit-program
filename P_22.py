n=input(": ")
n=n.lower()
flag=0
for i in range(len(n)):
    if n[i]==n[0]:
        flag+=1
print(flag)