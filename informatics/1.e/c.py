def xor(x,y):
    if(x==1 and y==1):return 0
    if(x==0 and y==0):return 0
    return 1
nums = list(map(int,input().split()))
n1=nums[0]
n2=nums[1]
print(xor(n1,n2))