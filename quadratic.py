
havePair = False
a=[1,2,4,4]
sum = 8
for i in range(1,len(a)):
    for j in range (i):
        if a[i]+a[j]== sum :
            print('Y',"Positional index:",j+1,i+1,"Number:",a[i],a[j])
            havePair = True
if not havePair:
    print('N')
