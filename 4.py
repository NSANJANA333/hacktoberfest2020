s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
p=[int(x) for x in input().split()[:m]]
o=[int(x) for x in input().split()[:n]]
y=[]
z=[]
g=0
h=0
for i in range(0,m):
    y.append(a+p[i])
for i in range(0,n):
    z.append(b+o[i])
for i in range(0,len(y)):
    if(y[i]>=s and y[i]<=t):
        g=g+1
print(g)
for i in range(0,len(z)):
    if(z[i]>=s and z[i]<=t):
        h=h+1

print(h)