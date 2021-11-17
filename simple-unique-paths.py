print ("Input size of room")
m=int(input("Count m:"))
n=int(input("Count n:"))


def paths(m, n):
    if (m<1 or n<1): return 0
    if (m==1 and n==1): return 1
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(m + 1):
        dp[1][i]=1
    for j in range(2,n+1):
        for i in range(1,m+1):
            dp[j][i] = dp[j-1][i]+dp[j][i-1]
    return dp[n][m]

print(paths(m,n))
