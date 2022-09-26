def pattern(n):
    for row in range(1,n+1):
        for column in range(1,n+1):
            print("*",end='')
        print(" ")

pattern(5)