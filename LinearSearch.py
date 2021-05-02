# Linear search

l=[2,5,7,34,7,598,45]
key=int(input("Enter a key to search "))
for x in l:
    if key==x:
        print(x ,'present')
        break
else:
    print(key,'is not present')
