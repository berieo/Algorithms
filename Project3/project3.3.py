"""

单源最短路径算法，因为有负权值，所以采用Bellman_Ford算法

"""

path = [
    [0,  -1,  3, 99, 99],
    [99,  0,  3,  2,  2],
    [99, 99,  0, 99, 99],
    [99,  1,  5,  0, 99],
    [99, 99, 99, -3,  0]
]


def bellman_ford(matrix):
    dis = [0, 99, 99, 99, 99]
    record = [
        ["A:"],
        ["B:"],
        ["C:"],
        ["D:"],
        ["E:"]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if dis[i] + matrix[i][j] < dis[j]:
                dis[j] = dis[i] + matrix[i][j]
                if i == 0:
                    record[j].append("A")
                elif i == 1:
                    record[j].append("B")
                elif i == 2:
                    record[j].append("C")
                elif i == 3:
                    record[j].append("D")
                elif i == 4:
                    record[j].append("E")

    print("到各点最短路径为：")
    print(record)
    print("到各点最短距离为：")
    print(dis)


bellman_ford(path)