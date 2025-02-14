
def solution(myString, pat):
    str1=""
    ls=[]
    for s in myString:
        if s == 'A': 
            str1 += 'B'
        else:
            str1 += 'A'
    return (1 if pat in str1 else 0)
    