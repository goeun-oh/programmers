def solution(arr):
    for i in range(len(arr)):
        arr[i]= arr[i]//2 if (arr[i]>=50 and arr[i]%2 ==0) else (arr[i] * 2 if (arr[i]%2 !=0 and arr[i]<50)  else arr[i])
    return arr