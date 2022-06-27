def solution(number):
    result = 0
    for i in range(1, number):
        if i%3==0 or i%5==0:
            result +=i
    return result
