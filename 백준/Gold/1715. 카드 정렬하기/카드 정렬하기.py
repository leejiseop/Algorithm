# 3:36

import heapq

answer = 0
n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(input()))

if n == 1:
  print(0)
else:
  for _ in range(n - 1):
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)
    sum = one + two
    answer += sum
    heapq.heappush(cards, sum)
  print(answer)

