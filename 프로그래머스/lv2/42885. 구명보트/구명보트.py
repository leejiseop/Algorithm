def solution(people, limit):
    answer = 0
    l = 0
    r = len(people) - 1
    people.sort()
    while l < r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        answer += 1
    if l == r:
        answer += 1
    return answer