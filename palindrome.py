n=int(input())
rev=0
temp=n
while(n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
if(temp==rev):
    print('yes')
else:
    print('no')
