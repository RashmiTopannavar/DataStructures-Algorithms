a = "WELCOME"
new_a = ''

for i in range(len(a)):
    lower_case = chr(ord(a[i])+32)
    new_a += lower_case

print(new_a)    