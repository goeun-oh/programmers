def solution(todo_list, finished):
    lst=[]
    lst.append(todo_list)
    lst.append(finished)
    answer=[lst[0][i] for i in range(len(lst[0])) if not lst[1][i]]
    return answer