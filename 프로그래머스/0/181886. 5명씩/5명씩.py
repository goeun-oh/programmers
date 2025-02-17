def solution(names):
    answer = [names[5*i] for i in range(((len(names)-1) // 5)+1)]
    return answer