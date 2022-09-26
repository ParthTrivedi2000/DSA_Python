# Q) print number form N to 1.

def num(n):
    if n==0:
        return
    print(n)
    num(n-1)

# num(5)

# Q) print number from 1 to N.

def number(n):
    if n==0:
        return
    number(n-1)
    print(n)

# number(5)

# Q) Print number from N to 1 and 1 to N.

def allNumber(n):
    if n==0:
        return
    print(n)
    allNumber(n-1)
    print(n)

# allNumber(5)


# Q) return the product of N to 1 numbers.

def product(n):
    if n<=1:
        return n
    return n*product(n-1)

# print(product(5))


# Q) Sum of N to 1:-

def suma(n):
    if n<=1:
        return n
    return n + suma(n-1)

print(suma(5))

