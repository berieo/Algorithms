"""

多源最短路径算法，采用Floyd算法，对每个点采用Bellman_ford算法的思路，
用二维数组记录下每两个点的最短距离和路径

"""
import numpy as np

path = [
    [0,  -1,  3, np.inf, np.inf],
    [np.inf,  0,  3,  2,  2],
    [np.inf, np.inf,  0, np.inf, np.inf],
    [np.inf,  1,  5,  0, np.inf],
    [np.inf, np.inf, np.inf, -3,  0]
]


def floyd(matrix):
    matrix = np.array(matrix)
    length = len(matrix)
    path = [list(range(length))] * len(matrix)
    path = np.array(path)
    print("原始路径矩阵：")
    print(matrix)

    for k in range(length):  # 可以经过k点
        for i in range(length):  # [i,j]点遍历
            for j in range(length):
                if matrix[i, j] > (matrix[i, k] + matrix[k, j]):
                    matrix[i, j] = matrix[i, k] + matrix[k, j]  # 两个顶点直接较小的间接路径替换较大的直接路径
                    path[i, j] = k
    print("最小距离矩阵：")
    print(matrix)
    print("最短路径矩阵：")
    print(path)


floyd(path)

