import math

def solution(n):
    answer = 1
    s = str(math.sqrt(n))
    if s.split('.')[1] != '0':
        answer=2
    return answer
