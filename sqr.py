
def sqrt_find(x):
    l=1
    h=x
    
    if(x==1 or x==0):
        return x
   
    while l<=h:
        mid=(l+h)//2
        if (mid*mid==x):
            return mid
        elif (mid*mid<x):
            l=mid+1
            
        else:
            h=mid-1
    return -1

x=int(input("enter a number: "))
reslt=print("Your target is in index: ",sqrt_find(x))

