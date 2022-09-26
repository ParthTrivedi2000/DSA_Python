# How to approach any pattern ?

# Step - 1] Run the outer for loop number of times you are having the lines. (similar in matrices. means
# as we know in matrices we are runninng outer for loop for 'row' and inner for loop for 'columns').

# Step - 2] Identify how many columns are there for every row. and also identify the types of elements each cell
# consists. (bec in some problems it was given *, in some #, in some patterns it's 1,2,3,4,5 etc etc).

# Step - 3] What do u need to print?(* or # or 1,2,3,4,5 etc etc)

# Note :- try to find the formula relating rows & columns

# code :-
def pattern(n):
    for row in range(1,n+1):
        # now for every row run the column
        for column in range(1,row+1):
            print("* ", end='') # end='' confirms that * should print in the same line
        # When one row is printed, we need to add a newline.
        print(" ")

# pattern(4)

def rev_pttern(n):
    for row in range(1,n+1):
        for column in range(1,n-row+2):
            print("*",end='')
        print("")

rev_pttern(5)