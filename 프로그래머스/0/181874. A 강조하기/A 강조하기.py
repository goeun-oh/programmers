def solution(myString):
    answer = ''
    myString=myString.replace('a', 'A')
    for s in myString:
        if ord(s) < ord('a') and ord(s) > ord('A'):
            myString=myString.replace(s, chr(ord(s) +32))
    return myString