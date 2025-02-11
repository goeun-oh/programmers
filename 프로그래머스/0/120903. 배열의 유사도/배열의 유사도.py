def solution(s1, s2):
    answer = 0
    ss= s1 if len(s1)< len(s2) else s2
    sl = s1 if len(s1)>=len(s2) else s2

    for i in range(len(ss)):
        if ss[i] in sl:
            answer+=1
    return answer