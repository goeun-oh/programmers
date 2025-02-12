def solution(my_string):
    answer = 0
    odn=[i for i in my_string if ord(i) >=48 and ord(i) <=57]
    for s in odn:
        answer += int(s)
    return answer