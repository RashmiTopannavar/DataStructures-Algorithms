def FindMissingElement(a):
    
    diff = a[0]- 0
    for i in range(len(a)):
        if a[i] - i != diff:
            return i+diff
        
    return -1    


a = [1,2,3,4,5,7,8]
result = FindMissingElement(a) 
if result != -1:
    print("Missing element is ", result)

else:
    print("No missing values found.")    




