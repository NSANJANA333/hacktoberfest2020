a=int(input())
for i in range(0,a):
    b,c=map(int,input().split())
    d=[int(x) for x in input().split()[:b]]
    e=0
    for i in range(0,b):
        for j in range(i+1,b):
            for y in range(j+1,b):
                if(d[i]+d[j]+d[y]==c):
                    e=e+1
            
    print(e)