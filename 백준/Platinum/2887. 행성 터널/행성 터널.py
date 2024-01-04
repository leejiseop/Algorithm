# 11:14 - 48

def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n = int(input())
parent = list(range(n + 1))

x = []
y = []
z = []

for i in range(1, n + 1):
  data = list(map(int, input().split()))
  x.append((data[0], i))
  y.append((data[1], i))
  z.append((data[2], i))

x.sort()
y.sort()
z.sort()

tunnels = []
answer = 0

for i in range(n - 1):
  tunnels.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1])) # (거리, a, b)
  tunnels.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
  tunnels.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))

tunnels.sort()

for cost, a, b in tunnels:
  if find_parent(parent, a) == find_parent(parent, b):
    continue
  union_parent(parent, a, b)
  answer += cost

print(answer)