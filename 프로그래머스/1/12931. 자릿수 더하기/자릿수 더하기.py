def solution(n):
    x = str(n)
    answer = 0
    for i in x:
        answer += int(i)
    return answer

print(solution(123))