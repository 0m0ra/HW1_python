k=int(input())
m=int(input())
n=int(input())
if k>=n:
    t=2*m
else:
    if (n%k)>0 and (n%k)<=3 or n-k==3:
        t=2*m*((n+k-1)//k)-m
    else:
        t=2*m*((n+k-1)//k)
print(t)
