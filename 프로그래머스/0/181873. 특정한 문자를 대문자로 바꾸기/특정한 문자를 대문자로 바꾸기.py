def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        my_string=my_string.replace(alp, chr(ord(alp)-32))
    return my_string