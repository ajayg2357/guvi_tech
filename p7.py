a=input()
a=list(a)
a[::2],a[1::2]=a[1::2],a[::2]
b="".join(a)
print(b)
