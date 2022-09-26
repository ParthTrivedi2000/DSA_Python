# Q) Sort the given array.

# [2,9,6,4,10,5,3]
def merge(arr1,arr2):  ## code for step-3
    mix = [0]*(len(arr1)+len(arr2))
    i = 0  # pointer 1 for arr1
    j = 0  # pointer 2 for arr2
    k = 0  # pointer for mix arr.
    while(i<=len(arr1)-1 and j<=len(arr2)-1):
        if arr1[i]<arr2[j]:
            mix[k] = arr1[i]
            i+=1
        else:
            mix[k] = arr2[j]
            j+=1
        k+=1
    # Now it may be possible that any of the one array is traversed till end still in another array few elements are
    # remaining. So that case is covered below. or if that will be the case, then call goes to either of
    # the below function
    while(i<=len(arr1)-1):
        mix[k] = arr1[i]
        i+=1
        k+=1
    while(j<=len(arr2)-1):
        mix[k] = arr2[j]
        j+=1
        k+=1
    return mix

def mergeSort(arr):

    if len(arr)==1:
        return arr
    mid = (len(arr)-1) // 2
    # Abhi yha pe me simply return mergeSort krke kruga to mera array 2 parts me divide nhi hoga. Bt muje to start se
    # mid tk and mid se end tk divide krna he. isliye me 2 seperate array ba rha hu.
    leftArray = mergeSort(arr[:mid+1])
    rightArray = mergeSort(arr[mid+1:])

    return merge(leftArray,rightArray)

l1 = [8,3,4,12,5,6]
print(mergeSort(l1))


# Solution -2) In place merge sort

def mergeInPlace(arr,start,mid,end):  ## code for step-3
    mix = [0]*(end-start)   # length of arr (end-start)
    i = start  # pointer 1 for virtual arr1.
    j = mid    # pointer 2 for virtual arr2
    k = 0      # pointer for mix arr.
    while(i<mid and j<end):
        if arr[i]<arr[j]:
            mix[k] = arr[i]
            i+=1
        else:
            mix[k] = arr[j]
            j+=1
        k+=1
    # Now it may be possible that any of the one array is traversed till end still in another array few elements are
    # remaining. So that case is covered below. or if that will be the case, then call goes to either of
    # the below function
    while(i<mid):
        mix[k] = arr[i]
        i+=1
        k+=1
    while(j<end):
        mix[k] = arr[j]
        j+=1
        k+=1

    # Previous case me to kya tha ki 2 separate array hi send kiye the merge functione ke ander merge krne ke liye to
    # usme me upr vale step tk krunga to bhi ho jayega. bt yha pe to jo actuall array he vhi he baki 2 parts to hmne
    # virtually soche he sirf. bt actual array me values change bhi to krni he. to vo ye below step se krenge.
    for l in range(0,len(mix)):
        arr[start+l] = mix[l] # yha pe start + l means vha se mera startin point hona chahiye. jese in neral case my
#         my starting point is 0 hota he means me 0 se nyi values add ya modified krni start krta hu isliye hm log alg
# se arr[0+k] nhi likhte he. bt yha pe muje change or modification index 0 se nhi krne he...bt recursive call me us time
# pe jo bhi start index ki value he vha se aage bdhte hue changes krne he isliye arr[start+l] likha he.

def mergeSortInPlace(arr,start,end):

    if (end-start)==1:
        return  # abhi me chnages original array me hi kr rha hu to muje kuch return krne ki jarurat nhi he means me
                # func ke bahar vapis ye vala arr print krke check kr lunga.
    mid = start + (end-start) // 2
    # Abhi yha pe me simply return mergeSort krke kruga to mera array 2 parts me divide nhi hoga. Bt muje to start se
    # mid tk and mid se end tk divide krna he. isliye me 2 separate array bna rha hu.
    mergeSortInPlace(arr,start,mid)
    mergeSortInPlace(arr,mid,end)

    mergeInPlace(arr,start,mid,end)

l1 = [8,3,4,12,5,6]
mergeSortInPlace(l1,0,len(l1))
print(l1)