N,Q=input().split()
N=int(N)
Q=int(Q)
s=[]
g=[]
h=[]
t=[]
a=input()
s.extend([int(x) for x in a.split()])
for j in range(0,Q):
    u,v=input().split()
    u=int(u)
    v=int(v)
    g.append(u)
    h.append(v)
for k in range(0,Q):
    t=s[(g[k]-1):(h[k])]
    n=0
    for l in range(0,len(t)):
        n=n^t[l]
    print(n)
