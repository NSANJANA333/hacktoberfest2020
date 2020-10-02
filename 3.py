a=int(input ())
c=[]
d=0
e=0
x=0
for i  in range(0,a) :
    b=[int(x) for x in input().split()[0:a]]
    c.append(b)
for i  in range(0,a):
    d=d+c[i][i]
    e=e+c[i][a-i-1]
print(abs(d-e)) 


            



