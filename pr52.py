x1,y1=input().split()
x2,y2=input().split()
x3,y3=input().split()
x4,y4=input().split()
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
x3=int(x3)
y3=int(y3)
x4=int(x4)
y4=int(y4)
a1=(((x2-x1)**2)+((y2-y1)**2))**(1/2)
a2=(((x3-x2)**2)+((y3-y2)**2))**(1/2)
a3=(((x4-x3)**2)+((y4-y3)**2))**(1/2)
a4=(((x4-x1)**2)+((y4-y1)**2))**(1/2)
if(a1==a2==a3==a4):
    print("yes")
else:
    print("no")
