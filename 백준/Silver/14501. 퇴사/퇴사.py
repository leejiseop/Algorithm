# 2:23

n = int(input())
t = []
p = []
max_val = 0

for _ in range(n):
  data = list(map(int, input().split()))
  t.append(data[0])
  p.append(data[1])
p.append(0)

for i in range(n - 1, -1, -1): # rev
  if i + t[i] <= n:
    p[i] = max(p[i] + p[i + t[i]], max_val)
    max_val = p[i]
  else:
    p[i] = max_val

print(p[0])