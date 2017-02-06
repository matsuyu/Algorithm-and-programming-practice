havePair = False
a=[1,2,4,4]
sum = 8
for i in range(len(a)):
    target = sum - a[i]
    low = 0
    high = len(a)-1
    mid = (low+high)//2
    while (low<high):
        if a[mid]==target:
            print("Y","Positional index:",i+1,mid+1,'Number:',a[i],target)
            havePair = True
            break
        elif a[mid]<target:
            low = mid +1
            mid = (low+high)//2
        else:
            high = mid-1
            mid = (low+high)//2
    if havePair:
        break
if not havePair:
    print("N")
