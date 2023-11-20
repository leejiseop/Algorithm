n = int(input())

dp = [0] * 1000001
sum = [0] * 1000001

dp[0] = 1
dp[1] = 2
dp[2] = 7

for i in range(3, n + 1):
  result = 2 * dp[i-1] + 3 * dp[i-2]
  sum[i] = sum[i-1] + 2 * dp[i-3]
  result += sum[i]
    
  dp[i] = result % 1000000007

print(dp[n])
