def calc_dp(n,k):
    arr = [[0 for i in range(k+1)] for j in range(n+1)]
    for i in range(n+1):
        arr[i][0]=1
    for i in range(k+1):
        arr[i][i]=1
    for i in range(1,n+1):
        for j in range(1,min(i-1,k)+1):
            arr[i][j]=arr[i-1][j]+arr[i-1][j-1]
    return arr[n][k]

