# 1:14

INF = 987654321

n = int(input())
soldiers = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

# n2 안에

for i in range(1, n + 1):
  for j in range(i):
    if soldiers[i] < soldiers[j]:
      dp[i] = max(dp[i], dp[j])
  dp[i] += 1

print(n - max(dp))