def solution(m, n, puddles):
    answer = 0
    # puddles = [[j, i] for [i, j] in puddles]
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    dp[1][1] = 1
    
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if [y, x] in puddles:
                continue
            dp[x][y] += dp[x-1][y] + dp[x][y-1]
    
    return dp[-1][-1] % 1000000007