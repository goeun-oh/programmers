def solution(price):
    answer = 0
    sales=[0, 0.05, 0.05, 0.1, 0.1, 0.2]
    k= min(price//100000,5)
    answer= int(price*(1-sales[k]))
    return answer