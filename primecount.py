a,b= input().split()
a=int(a)
b=int(b)
k=[]
for i in range(a,b+1):
    c=0
    for j in range(1,b+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        k.append(i)
print(len(k))
