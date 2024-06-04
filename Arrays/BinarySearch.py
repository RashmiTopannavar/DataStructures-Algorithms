a =[5]
key = 5
low=0
length = len(a)
high = length-1
found = False


while(low <= high):

    mid = (low+high)//2
    
    if key == a[mid]:
        found = True
        print(key, "is found at index " ,mid )
        break
    elif key<a[mid]:
        high = mid-1
    else:
        low = mid+1
        

if found == False:
    print("Key Not found")             
    



