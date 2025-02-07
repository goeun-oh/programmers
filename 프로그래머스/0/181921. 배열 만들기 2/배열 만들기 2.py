def solution(l, r):
    answer=[]
    answer2=generate_binary(100)

    final=[]
    for i in range(l,r+1):
        if i%5 ==0:
            answer.append(int(i/5))

    for i in range(len(answer)):
        for j in range(len(answer2)):
            if str(answer[i]) == str(answer2[j]):
                final.append(answer[i]*5)

    if not final:
        final.append(-1)
    return final

def generate_binary(n):
    list=[]
    for i in range(1, n+1):
        list.append(bin(i) [2:])
    return list
