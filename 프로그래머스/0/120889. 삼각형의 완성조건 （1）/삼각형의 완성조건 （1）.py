def solution(sides):
    max_values=sides.pop(sides.index(max(sides)))
    tot=0
    for i in sides:
        tot += i
    return 1 if tot> max_values else 2
