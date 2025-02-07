def multiply_matrix(mat1,mat2):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


def trans_matrix(mat):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            result[j][i] = mat[i][j]
    return result

def solution(matrix1,matrix2):
    multi_mat = multiply_matrix(matrix1,matrix2)
    
    return trans_matrix(multi_mat)

# TEST 코드

print(solution(
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
],

[
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]))


'''
반환값 : 
[
 [30, 84, 138],
 [24, 69, 114],
 [18, 54, 90]
]
'''

'''    
print(solution(
[
 [2, 4, 6],
 [1, 3, 5],
 [7, 8, 9]
],

[
 [9, 1, 2],
 [4, 5, 6],
 [7, 3, 8]
]))
'''

'''
반환값 : 
[
 [76, 56, 158],
 [40, 31, 74],
 [76, 60, 134]
]
'''