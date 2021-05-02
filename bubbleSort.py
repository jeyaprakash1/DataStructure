# Sort the list in ascending order using bubblee sort

l=eval(input("Enter a list"))
n=len(l)-1 #3
for y in range(0,n):
    for x in range(0,n):
        if l[x]>l[x+1]:
            l[x],l[x+1]=l[x+1],l[x]
    n-=1
print(l)
