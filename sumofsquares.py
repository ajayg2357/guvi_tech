a=int(input())
d=0;
while(a>=1):
    t=a%10
    d=d+(t*t)
    a=a//10
print(d)
