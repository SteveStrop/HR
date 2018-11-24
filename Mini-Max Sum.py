def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:-1]),sum(arr[1:]))


miniMaxSum([1, 2, 3, 4, 5])
