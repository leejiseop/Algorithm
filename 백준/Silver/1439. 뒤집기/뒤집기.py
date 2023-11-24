str = list(map(int, list(str(input()))))
i = 0
length = len(str)
count = 0

for i in range(length - 1):
  if str[i] != str[i + 1]:
    count += 1

if count % 2 != 0:
  count += 1
count //= 2

print(count)