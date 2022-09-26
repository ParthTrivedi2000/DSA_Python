# Method - 1 :- using 2-pointers

def palindrome(s,e,str):
    if s>=e:
        return print("It's palindrome")
    if str[s] == str[e]:
        palindrome(s+1,e-1,str)
    else:
        return print("Not palindrome")

# Method - 2 :- using 1-pointer only

def pali(i,str):
    if i>=len(str)//2:
        return True
    if str[i] != str[len(str)-i-1]:
        return False
    return pali(i+1,str)

str1 = '11211'
# x = palindrome(0,len(str1)-1,str1)
y = pali(0,str1)
print(y)