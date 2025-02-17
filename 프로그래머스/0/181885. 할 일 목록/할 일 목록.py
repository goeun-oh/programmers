def solution(todo_list, finished):
    answer=[task for i,task in enumerate(todo_list) if not finished[i]]
    return answer