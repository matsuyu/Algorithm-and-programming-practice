havePair = False
a=[1,2,4,4]
sum = 8
low = 0
high = len(a)-1
total = a[low]+a[high]
while (total!=sum) and (low<high):
    if total <sum:
        low+=1
        total =a[low]+a[high]
    elif total > sum:
        high-=1
        total = a[high]+a[low]
if total == sum:
    print('Y',"Positional index:",low+1,high+1,"Number:",a[low],a[high])
else:
    print('N')
