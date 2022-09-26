def splitArray(nums,m):
    start = 0
    end = 0

    start = max(nums)
    end = sum(nums)
    # Applying BS
    while(start<end):
        # try for the middle as potential answer which we want to find. or
        # So here we are jst assuming that I can partitioned the array with some subarrays which can have the
        # max value of sum of it's element is = mid
        mid = start + (end-start)//2

        # calculate how many pieces you can divide this array in, with the above max sum (which we have assumed as mid)
        # Actually why we are checking for pieces saperately?
        # bec in question m is given which must be the number of partition that we are doing.
        # But abhi to hmne uper vale max sum ke corresponding kitne partition ho skte he vo socha he.(jisko yha pe pieces bola he)
        # Suppose vo pieces actual given m  se jyada ya km aaye to we have to change pieces.

        suma = 0
        pieces = 1
        for num in nums:
            # agr sum of elements he vo hmare assumed max value se jyada ho gya to
            if (suma+num)>mid:
                # to we cannot add this element in this partition or subarray (partition ya to subarray
                # actual me nhi bnane he is liye code me nya subarray create nhi kiya he vo hme visually
                # imagine krna he means sari process krke sirf largest sum hi return krna he that's our motive)

                # So agr ye element is subarray me nhi add kr skte then we have to make new subarray which
                # is starting from that element only (or not include any previous elements)
                suma = num
                pieces = pieces + 1
            else:
                suma = suma + num

        # Now we are applying check on pieces
        if pieces>m:
            start = mid + 1
        else:
            end = mid
    return end             # as we want to return that largest sum while all the conditions met so returning it
                           # here you can return start also as start == end.

l1 = [7,2,5,10,8]
partition = 2
print(splitArray(l1,partition))