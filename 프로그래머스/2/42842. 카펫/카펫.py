def solution(brown, yellow):
    tot = brown + yellow
    for i in range(3, tot):
        if tot % i == 0 :
            width = i
            height = int(tot/i)
            if (width - 2) * (height - 2) == yellow and width >= height:
                return [width, height]