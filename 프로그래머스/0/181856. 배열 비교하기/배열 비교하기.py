def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        answer=1 if sum(arr1)> sum(arr2) else (-1 if sum(arr1) < sum(arr2) else 0)
        
    else:
        answer=1 if len(arr1) > len(arr2) else -1 
    return answer