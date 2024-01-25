s = list(map(int, input()))

count_0 = 0
count_1 = 0
current = 999

for digit in s:
  if digit == current:
    continue
  if digit == 0:
    count_0 += 1
  else:
    count_1 += 1
  current = digit

print(min(count_0, count_1))