"""

最短路径问题，采用Dijistra算法解决

"""

import numpy as np

#                  0   1   2   3   4   5   6   7   8   9   10  11  12 13  14   15
graph = np.array([[0,  5,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [5,  0,  0,  1,  3,  6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [3, -1,  0, -1,  8,  7,  6, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                  [-1, 1, -1,  0, -1, -1, -1,  6,  8, -1, -1, -1, -1, -1, -1, -1],
                  [-1, 3,  8, -1,  0, -1, -1,  3,  5, -1, -1, -1, -1, -1, -1, -1],
                  [-1, 6,  7, -1, -1,  0, -1, -1,  3,  3, -1, -1, -1, -1, -1, -1],
                  [-1,-1,  6, -1, -1, -1,  0, -1,  8,  4, -1, -1, -1, -1, -1, -1],
                  [-1,-1, -1,  6,  3, -1, -1,  0, -1, -1,  2,  2, -1, -1, -1, -1],
                  [-1,-1, -1,  8,  5,  3,  8, -1,  0, -1, -1,  1,  2, -1, -1, -1],
                  [-1,-1, -1, -1, -1,  3,  4, -1, -1,  0, -1,  3,  3, -1, -1, -1],
                  [-1,-1, -1, -1, -1, -1, -1,  2, -1, -1,  0, -1, -1,  3,  5, -1],
                  [-1,-1, -1, -1, -1, -1, -1,  2,  1, -1, -1,  0, -1,  5,  2, -1],
                  [-1,-1, -1, -1, -1, -1, -1, -1,  2,  3, -1, -1,  0,  6,  6, -1],
                  [-1,-1, -1, -1, -1, -1, -1, -1, -1, -1,  3,  5, -1,  0, -1,  4],
                  [-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  2,  6, -1,  0,  3],
                  [-1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  4,  3,  0]])


def shortest_path(matrix):
    S = np.zeros(len(matrix), dtype=int)
    index = 0

    # -1置为最大
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                matrix[i][j] = 99

    dis = matrix[0]
    while index < len(matrix):
        minimum = 99
        # 挑出每一行中最小值
        for x in range(1, len(dis)):
            if dis[x] < minimum:
                if x not in S:
                    minimum = dis[x]
                    i = x
        S[index] = i
        index += 1
        for j in range(0, len(matrix)):
            if matrix[i][j] != 0:
                if dis[i] + matrix[i][j] < dis[j]:
                    dis[j] = dis[i] + matrix[i][j]
    print("最短距离数组：")
    print(dis)
    print("已经计算的数组：")
    print(S)
    return dis,S


# 采用递归找出最短路径
def find_path(matrix, dis, S, record):
    last = []
    minimum = 99
    for i in record:
        for j in range(len(matrix)):

            # 记录和最后一个元素相邻的元素
            if matrix[i][j] != 0 and matrix[i][j] != 99:
                last.append(j)

    # 记录响相邻元素中距离最小的值
    for x in last:
        if minimum > dis[x]:
            minimum = dis[x]

    # 距离最小的值的下标
    for x in last:
        if dis[x] == minimum:
            if x == 0:
                record.append(0)
                return
            else:
                record.append(x)
                find_path(matrix, dis, S, record)
    print(record)


dis , S = shortest_path(graph)
record = []
record.append(len(graph) - 1)
find_path(graph, dis, S, record)


