def isPalindrome(s):
    s = s.lower()
    a = ""
    for i in range(len(s)):
        if (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
            a+= s[i]

    if (a == a[::-1]):

        return True
    else:
        return False
             
        

        
            
     


s = " "   
res = isPalindrome(s)
print(res)    
        