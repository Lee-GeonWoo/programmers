def solution(n):
    n = n ** 0.5
    
    if n == int(n):
        answer = (n + 1) ** 2
    else:
        answer = -1
    return answer
