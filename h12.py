a,b=input().split()
a=int(a)
b=int(b)
for i in range(a):
    x=input().split()
    x.sort(key=int)
    y=x[::-1]
    break
z=y.pop(b-1)
z=int(z)
print(z)
