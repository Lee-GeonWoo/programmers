def solution(n):
    answer = 1
    
    while n % answer != 1:
        answer += 1
    
    return answer
