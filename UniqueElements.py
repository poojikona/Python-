n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n):
    c=0
    for j in range(n):
        if(arr[i]==arr[j]):
            c=c+1
    if c==1:
        l.append(arr[i])
print(" ".join(map(str,l)))
