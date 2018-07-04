n=int(input())
k=int(input())
m=list(range(1,n+1))
c=0
for i in range(k):
    c=c+m[i]
    print(c)
