def solution(my_string):
    answer = ''
    for s in my_string:
        if ord('a') <= ord(f'{s}'):
            answer += chr(ord(f'{s}')-32)
        else:
            answer += chr(ord(f'{s}') + 32)
    return answer