# Pivot :- choose any element as pivot
# What quick sort is doing? (or logic or approach of quick sort algorithm towards sorting the array)
# after 1st pass --> all the elements of array which are < Pivot will be on L.H.S. of pivot. and
# all the elements of array which are > Pivot will be on R.H.S. of pivot.
# Pls note here those elements which comes on LHS or RH may or ay not be in the sorted order. but after 1st pass
# my one element (pivot) is at it's correct place in sorting order.

# Now main question is how to put pivot element at it's correct position ?
# So what we will doing is as we know element at the start and all the elements at the left side of pivot should be
# less than pivot element. and element at end index and towards end it means all the element at the right side of pivot
# element should be greater than pivot element ideally. So this should be our logic ki jha pe ye cheeze ka violation (i.
# e. if any value left on the pivot is greater than pivot or any value which ais on right of the pivot is less than
# pivot ) then we will jst swap the elements and send the elements to their appropriate side. so both the swapped values
# are now at it's appropriate side.

def quickSort(arr,low,high):
    if low>=high:
        return

    start = low
    end = high
    mid = start + (end-start)//2
    pivot = arr[mid]

    while (start<=end):
        while(arr[start]<pivot):
            start += 1
        while(arr[end]>pivot):
            end -= 1
        if(start<=end):
            temp = arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start += 1
            end -= 1

        # now my pivot is at correct index, please sort two halves of array now.
        quickSort(arr,low,end)
        quickSort(arr,start,high)

l1 = [3,6,4,4,5,2,1]
quickSort(l1,0,len(l1)-1)
print(l1)