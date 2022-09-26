# 0,1,1,2,3,5,8,13,21,34,55,89,144

# 1-->4
# 2-->7
# 3-->10
# 4-->13
n = int(input("Enter the number : "))
p = (3 * n) + 1


def even(x):
    if x <= 2:
        return x - 1
    else:
        return even(x - 1) + even(x - 2)


y = even(p)
print(y)
