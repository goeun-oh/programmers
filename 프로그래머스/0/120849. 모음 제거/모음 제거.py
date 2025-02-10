def solution(my_string):
    answer = ''
    list0=['a','e','i','o','u']
    my_string=list(my_string)
    for s in list0:
        while(s in my_string):
            my_string.remove(s)
    for i in range(len(my_string)):    
        answer += my_string[i]
    return answer