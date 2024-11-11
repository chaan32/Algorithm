# def solution(s):
#     cnt = 0
#     zero = 0
#     while s!="1":
#         print(s)
#         before_len = len(s)
#         after_len = 0
#         for i in s:
#             if s == "1":
#                 after_len+=1
#         zero += before_len - after_len
#         s = format(after_len, 'b')
#         cnt += 1
        
#     return [cnt, zero]

def solution(s):
    cnt = 0
    zero = 0
    while s!="1":
        after_len = len(s) - s.count("0")
        zero += s.count("0")
        s = format(after_len, 'b')
        cnt += 1
        
    return [cnt, zero]