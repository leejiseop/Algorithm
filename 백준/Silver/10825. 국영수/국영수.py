import sys
#1:12
f = sys.stdin.readline

n = int(input())
students = []
for _ in range(n):
  students.append(list(f().split()))

students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for name, kor, eng, math in students:
  print(name)