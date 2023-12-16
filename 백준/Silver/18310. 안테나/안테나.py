# 2:17

n = int(input()) # 1 ≤ N ≤ 200,000
house_list = list(map(int, input().split()))

house_list.sort()
print(house_list[(n - 1) // 2])