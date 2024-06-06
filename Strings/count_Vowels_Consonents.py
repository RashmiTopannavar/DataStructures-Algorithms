def count_Vowels_Consonents(a):
    vcount = 0
    ccount = 0

    for i in range(len(a)):
        if a[i] in 'aeiouAEIOU':
            vcount += 1
         
    
        elif (ord(a[i]) >= 97 and ord(a[i]) <= 122) or (ord(a[i]) >= 65 and ord(a[i]) <= 90):
            ccount+= 1 
    return ccount, vcount
        
a = "Hello world"
consonents, vowels = count_Vowels_Consonents(a)
print("consonents: ", consonents, "vowels: ", vowels)


