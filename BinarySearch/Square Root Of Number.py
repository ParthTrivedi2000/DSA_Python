def sqrt(num):
    start = 1
    end = num
    ans = 0
    while (start <= end):
        mid = start + (end - start) // 2
        if (mid * mid) > num:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans
# x = sqrt(37)
# print(x)

# Suppose interviwer ask he needs precise value of sqrt of number. Below is the code.

def morePrecise(num, precision, x):
    factor = 1
    ans = x
    i = 0
    while(i<precision):
        factor = factor/10
        j = ans
        while(j*j<num):
            ans = j
            j = j+factor
        i = i + 1
    return ans             # here u also can use round(ans,precision) to limit the number after decimal.

x = sqrt(37)
mainAnswer = morePrecise(37,3,x)
print(mainAnswer)