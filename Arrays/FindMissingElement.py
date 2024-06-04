def FindMissingElement(a):
    
    diff = a[0]- 0
    for i in range(len(a)):
        if a[i] - i != diff:
            return i+diff
        
    return -1    


a = [1,2,3,4,5,6,7,8]
result = FindMissingElement(a) 
if result != -1:
    print("Missing element is ", result)

else:
    print("No missing values found.")    


#######################################################################################################################################

def FindMissingElement_SumApproach(a):
    sum = 0
    a_len = len(a) + 1  # +1 cuz 1 element in the array is missing
    print("length of array", a_len)

    for i in range(len(a)):
        sum = sum + a[i]

    s_formula = a_len * (a_len+1)//2     #[n*(n+1)]/2
    print("formula value ",s_formula)

    missingElement = s_formula - sum  

    return missingElement

    


a = [1,2,3,4,5,6,7,8,9]
result = FindMissingElement_SumApproach(a)
print(result)



