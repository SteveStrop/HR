n = 3
arr=[
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]
def diagonalDifference(arr):
    p=0
    s=0
    for i in range(n):
        p+=(arr[i][i])
        s+=(arr[i][n-1-i])
    return abs(p-s)

print(diagonalDifference(arr))
