n = int(input())

dp = [0] * 31

dp[0] = 1
dp[1] = 0
dp[2] = 3
dp[3] = 0

for i in range(4, n + 1):
  if i % 2 == 0:
    result = 3 * dp[i-2]
    for j in range(0, i - 4 + 1, 2):
      result += 2 * dp[j]
    dp[i] = result
  else:
    dp[i] = 0

print(dp[n])
