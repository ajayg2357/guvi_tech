a=int(input())
res=0
while(a>0):
    x=a%10
    res=res+x**2
    a=a//10
print(res)
