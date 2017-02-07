havePair = False
a=[1,2,4,4]
dic = {}
sum = 8
for i in range ( len(a )):
    if a[i] in dic:
        print('Y',"Positional index:",dic[a[i]]+1,i+1,"Number:",a[dic[a[i]]+1],a[i])
        havePair= True
        break
    else:
        dic[sum-a[i]]=i
if not havePair:
    print('N')
    for key,value in dic.items():
        print (key,value)
