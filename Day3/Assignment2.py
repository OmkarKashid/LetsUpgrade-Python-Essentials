n=int(input())
flag=True
if n>2:
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
            break
if n<2:
    flag=False
if flag==True or n==2:
    print("Prime number")
else:
    print("Not a prime number")