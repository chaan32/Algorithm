# 귤 크기 별로 빈도를 계산해야 함 -> ok
# 빈도를 내림차순으로 정렬 해야 함 ->

def solution(k, tangerine):
    tan = {}
    for t in tangerine:
        if t in tan : #값 추가
            tan[t]+=1
        else : #생성
            tan[t]=1
    tan_re = sorted(tan.values(), reverse=True)
    kind = 0
    cnt = 0
    for i in tan_re:
        kind+=1
        cnt+=i
        if cnt >= k:
          break
    return kind





















