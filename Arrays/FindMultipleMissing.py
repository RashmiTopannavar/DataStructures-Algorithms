def findMultipleMissing(a):
    diff = a[0]  - 0
    b = []

    for i in range(len(a)):
        if a[i]-i != diff :
            while a[i] - i > diff:
                b.append(i+diff)
                diff = diff+1
    return b
            
    

# a = [6,7,8,9,11,12,15,16,17,18,19]
# # a = [6,7,8,9]
# res = findMultipleMissing(a)
# if res == []:
#     print("No missing element")
# else:
#     print(res)


def findMissing_Hash(a):
    dict_Hash = {}
    b = []
    low =  min(a)
    high = max(a)

    for i in a:
        dict_Hash[i] = 1

    for i in range(low, high):
        if i not in dict_Hash:
            b.append(i)

    return b

a = [2,6,7,8,9,11,12,15,16,17,18,19]
res = findMissing_Hash(a)
if res == []:
    print("No missing element")
else:
    print(res)

            



                
