import math
def solution(a, b, c, d):
    answer = 0
    if a == b == c == d:
        answer+= 1111*a
    elif (a == b == c) or (a == b == d) or (a == c == d) or (b == c == d):
        if a == b == c:
            answer+=(10*a+d)**2
        elif a == b == d:
            answer+=(10*a+c)**2
        elif a == c == d:
            answer+=(10*a+b)**2
        elif (b == c == d):
            answer += (10*b+a)**2
    elif (a == b) or (a == c) or (a == d) or (b == c) or (b == d) or (c == d):
        if (a == b) or (c==d):
            if (a==b) and (c==d):
                answer+=(a+c)*abs(a-c)
            elif (a==b) and (c!=d):
                answer+=c*d
            else:
                answer=a*b

        elif (a == c) or (b == d):
            if (a==c) and (b==d):
                answer += (a + b) * abs(a - b)
            elif (a==c) and (b!=d):
                answer+=b*d
            else:
                answer+=a*c

        elif (a == d) or (b ==c):
            if (a==d) and(b==c):
                answer += (a + b) * abs(a - b)
            elif (a==d) and (b!=c):
                answer+=b*c
            else:
                answer+=a*d

    else:
        list=[]
        list.append(a)
        list.append(b)
        list.append(c)
        list.append(d)
        answer=min(list)

    return answer
