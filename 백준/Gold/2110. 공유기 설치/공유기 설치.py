n, c = map(int, input().split())
houses = []
for _ in range(n):
  houses.append(int(input()))
houses.sort()


### answer ###

start = 1 # 최소거리 : 1
end = houses[-1] - houses[0] # 최대거리 : 집 최장 거리

# start = houses[0]
# end = houses[-1]

result = 0

while start <= end:
  mid = (start + end) // 2 # 최소범위 설정
  set_house = houses[0] # 맨 앞집에

  # mid = (end - start + 1) // 2 # 최소 거리
  # set_house = houses[0] # 앞 공유기

  count = 1

  for i in range(1, n): # 나머지 집들 탐색
    if set_house + mid <= houses[i]: # 최소범위보다 멀면
      set_house = houses[i] # 설치하고
      count += 1 # 설치 수 증가
      
  if c <= count: # 딱맞게 설치됐거나 많이 설치됐으면
    result = mid # 일단 저장하고
    start = mid + 1 # 최대범위를 찾아야 하니 범위 늘려서 다시 탐색
  else: # 적게 설치됐으면
    end = mid - 1 # 범위 좁혀서 다시 탐색

print(result)
