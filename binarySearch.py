# Binary search

l=[0,10,20,40,50,70,85,91,96,97,100,130]
key=int(input("Enter a key "))
min=0
max=len(l)-1

while min<=max:
    mid=(min+max)//2
    if key==l[mid]:
        print(key,'is present at',mid)
        break
    elif key>l[mid]:
        min=mid+1
    else:
        max=mid-1
else:
    print(key, 'is not present')
