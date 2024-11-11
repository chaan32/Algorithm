def solution(n):
    n_binary = format(n, 'b')
    tar = n + 1
    while True:
        tar_binary = format(tar, 'b')
        print(f"target : {tar} bina : {tar_binary}")
        if n_binary.count("1") == tar_binary.count("1") :
            return tar
        tar+=1