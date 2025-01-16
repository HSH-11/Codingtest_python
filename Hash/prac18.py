def count_sort(arr,k): #O(N+K)
    hashtable = [0] * (k+1)

    for num in arr:
        if num <= k:
            hashtable[num] = 1
    
    return hashtable

def solution(arr, target): #O(N)
    hashtable = count_sort(arr,target)

    for num in arr:
        complement = target - num
        if (
            complement != num
            and complement >= 0
            and complement <= target
            and hashtable[complement] == 1
        ):
            return True
    return False
# TEST 코드
print(solution([1, 2, 3, 4, 8], 6)) # 반환값 : True
print(solution([2, 3, 5, 9], 10)) # 반환값 : False