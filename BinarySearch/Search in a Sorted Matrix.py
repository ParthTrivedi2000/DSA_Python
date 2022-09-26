def binarySearch(arr,target):
    row_length = len(matrix)
    col_length = len(matrix[1])
    row_iterator = 0
    col_iterator = len(matrix[1]) - 1
    while(row_iterator>=0 and row_iterator<row_length and col_iterator>=0 and col_iterator<col_length):
        if arr[row_iterator][col_iterator] == target:
            return [row_iterator,col_iterator]
        elif arr[row_iterator][col_iterator] > target:
            col_iterator = col_iterator - 1
        elif arr[row_iterator][col_iterator] < target:
            row_iterator = row_iterator + 1
    return [-1,-1]

matrix = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
num = 29
print(binarySearch(matrix,num))
