def solution(my_string):
    answer = ''
    A=['a','e','i','o','u']
    for s in A:
            my_string=my_string.replace(s, '')
    answer=my_string
    return answer