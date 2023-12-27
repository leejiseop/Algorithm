# 12:40

n = int(input())
soldiers = list(map(int, input().split()))
dp = [0] * n
temp = 0

for i in range(n):
  for j in range(i):
    if soldiers[i] < soldiers[j]:
      temp = max(temp, dp[j])
  dp[i] = temp + 1
  temp = 0

print(n - max(dp))
