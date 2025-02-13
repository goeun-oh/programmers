def solution(arr, n):
    answer = []
    if len(arr)%2==0:
        for i in range(len(arr)):
            answer.append(arr[i]) if i%2 ==0 else answer.append(arr[i]+n)
    else:
        for i in range(len(arr)):
            answer.append(arr[i]) if i%2 !=0 else answer.append(arr[i]+n)
            
    return answer