def solution(my_string):
    answer = [int(s) for s in my_string if ord(s)>=48 and ord(s)<=57]
    answer.sort()
    return answer