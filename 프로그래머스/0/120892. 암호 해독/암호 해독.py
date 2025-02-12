def solution(cipher, code):
    cipher=list(cipher)
    answer=''.join([cipher[i] for i in range(len(cipher)) if (i+1)%code ==0])
    return answer