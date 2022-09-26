# Q) reverse a number. for exa: 1234 --> 4321. 1842--> 2481.

# Solutio - 2 :-
# When we need to return value or when to print?
# we need to return a value whenever variables's value has been calculated iside a fuctio.
# So here we have declared a variable out side the function and accumulate the value in outide variable oly.

# globals(suma)
suma = 0
def reverse1(m):
    global suma
    if m == 0:
        return;
    rem = m%10
    suma = suma*10 + rem
    reverse1(m/10)

reverse1(1234)
print(suma)

# Soln - 2:
# Sometimes you might need some additional variables in the argument in that case, we can make another function.
import math


def helper(n,digits):
    if n%10 == n:
        return
    reminder = n%10
    return reminder*pow(10,digits - 1) + helper(n/10,digits-1)
def reverse(n):
    digits = math.log10(n) + 1
    return helper(n,digits)

print(reverse(1234))


# Soln:-3 :- by me

def rec(n):
    if n//10 == 0:
        return n
    return (n%10)*pow(10,int(math.log10(n))) + rec(n//10)

# Q) Check whether the give umber is palindrome or not?

def pali(m):
    return m == reverse(m)