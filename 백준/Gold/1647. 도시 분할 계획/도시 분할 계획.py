# 11:35  11:45

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

n, m = map(int, input().split()) # 집 개수, 길 개수
parent = list(range(n + 1)) # 0번 + 1번부터 n번까지
result = 0
max_cost = 0

edges = []
for _ in range(m):
  edges.append(list(map(int, input().split())))
edges.sort(key = lambda x: x[2]) # 유지비 순 정렬

for a, b, cost in edges:
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    max_cost = cost

print(result - max_cost)