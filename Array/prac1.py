def solution(arr):
  arr.sort() #O(nlogn)
  return arr
  
# TEST 코드
# print(solution([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
# print(solution([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
# print(solution([1,6,7])) # 반환값 : [1, 6, 7]

#버블 정렬 O(n**2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
  