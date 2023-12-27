n = int(input())
t = [0]
p = [0]
dp = [0] * (1 + n + 1)
max_val = 0

for _ in range(n):
  data = list(map(int, input().split()))
  t.append(data[0])
  p.append(data[1])

for i in range(n, 0, -1): # rev
  time = i + t[i]
  if time <= n + 1:
    dp[i] = max(p[i] + dp[time], max_val)
    max_val = dp[i]
  else:
    dp[i] = max_val

print(dp[1])