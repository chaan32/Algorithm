def solution(s):
        stack = []
        size = -1
        for i in range(len(s)):
             if size == -1:
                 stack.append(s[i])
                 size+=1
             elif stack[size] == s[i]:
                 del stack[size]
                 size-=1
             elif stack[size] != s[i]:
                 stack.append(s[i])
                 size+=1

        if size==-1 :
            return 1
        return 0