a=int(input())
for i in range(0,a):
    b=int(input())
    c=[int(x) for x in input().split()[0:b]]
    c=sorted(c)
    y=0
    for i in range(0,b):
        d=0
        for j in range(0,b):
            if(c[i]==c[j]):
                d=d+1
    if(d==1):
        print(c[i])
                
        