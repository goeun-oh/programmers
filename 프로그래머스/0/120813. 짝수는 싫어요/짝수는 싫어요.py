def solution(n):
    answer =[2*i+1for i in range(0,n//2 if n%2 ==0 else n//2 +1)]
        
    return answer
