# Q) Sum of the digits of a number.

def digitSum(n):
    if (n//10==0):
        return n
    return n%10 + digitSum(n//10)

print(digitSum(1234))


# Q) Product of the digits of a number.

def digitProduct(n):
    if (n//10==0):
        return n
    return n%10 * digitProduct(n//10)

print(digitProduct(1234))

# One thing to note is whenever question regarding digits will come, we have to play with or use n%10 and n//10
# things. So you should start thinking for an aproach about using these both, in any of the digit questions.