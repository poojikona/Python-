n=int(input())
for i in range(n):
    for j in range(2*n):
        if (i!=0 and (j==i or j==2*n-i-1)):
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
