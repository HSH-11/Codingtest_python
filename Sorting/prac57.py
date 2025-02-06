def solution(n):#시간 복잡도 O(logN*log(logN))
    digits = list(str(n)) #주어진 숫자의 자리수 logN
    digits.sort(reverse=True) #sort-> N개일 때 logN이므로 N이logN이면 logN*log(logN)
    answer = int("".join(digits))
    return answer