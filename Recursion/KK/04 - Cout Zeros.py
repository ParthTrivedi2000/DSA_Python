# Q) Count the number of zeros in a number.
# This is the very important question to understand how answer is returned to it's above
# function calls and the last final call.

# so here remember this concept of how to pass a value to above calls in recursion.
# When to use helper function or Why are we taking helper function?
# bec we want to pass extra args in the argument itself that's why we are using helper function.
# bec whenever u r using any platform
# in that they will provide a function with args. bt to provide the solution we need more args
# to pass in the function so we can make helper function and do the things as per our needs.

# Soln - 1 :- count is passed in args.
def helper(m,c):
    if m//10==0:
        return c
    if m%10 == 0:
        return helper(m//10,c+1)
    return helper(m//10,c)

def cout(m):
    return helper(m,0)

x = cout(30820)
# print(cout(30203054))
print(x)