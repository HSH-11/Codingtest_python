def solution(lst):
    unique_lst = list(set(lst)) #set 함수는 해시 알고리즘(O(1))으로 중복을 제거하는데 시간 복잡도가 O(N)을 보장
    unique_lst.sort(reverse=True) #중복원소 제거 O(N)하고 다시 정렬하는데 O(NlogN)이므로 최종적으로 O(NlogN)
    return unique_lst

# TEST 코드
# print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
# print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]

"""일반적으로 반복문을 통해 중복을 제거하는 알고리즘은 시간 복잡도가 O(n**2)으로 성능이 좋지 않다."""