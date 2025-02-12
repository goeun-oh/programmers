def solution(rsp):
    n=[0,5,2]
    answer = ''
    for s in rsp:
        answer+=f'{n[((int(s)%4)+1)%3]}'
    return answer