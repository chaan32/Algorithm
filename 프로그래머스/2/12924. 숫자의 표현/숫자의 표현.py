def solution(n):
    cnt = 0
    for i in range(1, n+1) :
        tot = 0
        for j in range(i, n+1) :
            tot += j
            if tot == n :
                cnt +=1
                break
            elif tot > n :
                break
    return cnt
            