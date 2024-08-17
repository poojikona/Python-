n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(i,n):
        if(arr[i]==arr[j]):
            c+=1
    if c==2:
        print(arr[i])
    
