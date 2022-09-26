def swapping(arr,first,second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    return arr


def getMaxIndex(arr,start,end):
    max = start
    for i in range(start,end + 1):
        if arr[i]>arr[max]:
            max = i
    return max


def bubble(arr):
    # run the steps n-1 times. i is the counter for how many times we have to run the loop.
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j]>arr[j+1]:
                swapping(arr,j,j+1)
                swapped = True
        if (swapped is False): #for any ith iteration, if j never swaps for a value of i, it means
            # array is sorted, hence you can end the program.
            break
    return arr


def selection(arr):
    for i in range(len(arr)):
        # find the max element from the remaining array and swap with correct index
        last = len(arr) - i - 1
        maxIndex = getMaxIndex(arr, 0, last)
        swapping(arr,maxIndex,last)
    return arr


def insertion_sort(arr):
    # outer loop will run n-2 times so
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j]<arr[j-1]:
                swapping(arr,j,j-1)
            else:
                break
    return arr


a1 = [-18,35,23,0,45,-2,-32]
x = insertion_sort(a1)
print(x)