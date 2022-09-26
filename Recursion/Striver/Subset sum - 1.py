def SumArray(index,sm,array,ds,smarray):
    if index==len(array):
        smarray.append(sm)
        # print(smarray)
        return
    ds.append(array[index])
    SumArray(index+1,sm+array[index],array,ds,smarray)
    ds.remove(ds[len(ds)-1])
    SumArray(index+1,sm,array,ds,smarray)

ar1 = [3,1,2]
l1 = []
sm1 = []
x = SumArray(0,0,ar1,l1,sm1)
print(sm1)