"""

最长公共子串问题，采用推导图的思路来解决

"""
import numpy as np

X1 = ["", "x", "z", "y", "z", "z", "y", "x"]
Y1 = ["", "z", "x", "y", "y", "z", "x", "z"]
X2 = ["", "M", "A", "E", "E", "E", "V", "A", "K", "L", "E", "K", "H", "L", "M", "L", "L", "R", "Q", "E", "Y", "V", "K", "L", "Q", "K", "K", "L", "A", "E", "T", "E", "K", "R", "C", "A", "L", "L", "A", "A", "Q", "A", "N", "K", "E", "S", "S", "S", "E", "S", "F", "I", "S", "R", "L", "L", "A", "I", "V", "A", "D"]
Y2 = ["", "M", "A", "E", "E", "E", "V", "A", "K", "L", "E", "K", "H", "L", "M", "L", "L", "R", "Q", "E", "Y", "V", "K", "L", "Q", "K", "K", "L", "A", "E", "T", "E", "K", "R", "C", "T", "L", "L", "A", "A", "Q", "A", "N", "K", "E", "N", "S", "N", "E", "S", "F", "I", "S", "R", "L", "L", "A", "I", "V", "A", "G"]
X3 = ["", "A", "B", "C", "A", "D", "B", "B"]
Y3 = ["", "B", "C", "E", "D", "B", "B"]


def longest_common_substring(X, Y):

    c = np.zeros((len(X), len(Y)))
    maximum = np.dtype(np.float64)
    maximum = 0
    max_i = 0
    max_j = 0

    # 从左到右，从上到下开始比较
    for i in range(1, len(X)):
        for j in range(1, len(Y)):

            # 比较X,Y,若相等取左上+1
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1

                # 如果此时比最大记录值大，则记录当前值
                if c[i][j] > maximum:
                    maximum = c[i][j]
                    max_i = i
                    max_j = j

    ans = []
    temp = []
    maximum = int(maximum)
    for x in range(maximum, 0, -1):
        temp.append(X[max_i])
        max_i -= 1
        max_j -= 1

    # 将暂存的倒序值赋给ans数组
    for x in range(len(temp)-1, -1, -1):
        ans.append(temp[x])

    print("===============================")
    print("最长公共子串为：")
    print(ans)
    print("长度为：")
    print(maximum)
    print("===============================")


longest_common_substring(X1, Y1)
longest_common_substring(X2, Y2)