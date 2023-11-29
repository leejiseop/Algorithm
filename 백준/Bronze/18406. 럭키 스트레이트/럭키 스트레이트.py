n = list(map(int, input()))
length = len(n)

if sum(n[:length//2]) == sum(n[length//2:]):
  print('LUCKY')
else:
  print('READY')