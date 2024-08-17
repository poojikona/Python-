n=int(input())
num=len(str(n))
arm_sum=0
temp=n
while temp>0:
    d=temp%10
    arm_sum+=d**num
    temp//=10
if arm_sum==n:
    print("YES")
else:
    print("NO")
