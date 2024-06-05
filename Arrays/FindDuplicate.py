def FindDuplicate(a):
    lastDup = []
    for i in range(len(a)-1):
        if a[i] == a[i+1] and a[i] not in lastDup:
            lastDup.append(a[i])
    return lastDup
    
# return -1    

a = [1,2,2,3,4,4,5,5]
res = FindDuplicate(a)
print(res)