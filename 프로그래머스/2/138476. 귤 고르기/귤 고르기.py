def solution(k, tangerine):
    # 각 귤 크기의 빈도를 저장할 딕셔너리 생성
    d = {}
    for size in tangerine:
        if size in d:        # tangerine이 아니라 d에서 확인해야 함
            d[size] += 1
        else:
            d[size] = 1

    # 빈도를 내림차순으로 정렬
    c = sorted(d.values(), reverse=True)

    total = 0
    kind_count = 0  # 종류 수 초기화
    for count in c:
        total += count
        kind_count += 1
        if total >= k:
            break

    return kind_count
























