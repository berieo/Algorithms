"""

最长公共子序列问题，的解决方案有暴力枚举，采用推导图的思路来解决

"""
import numpy as np

X1 = ["", "x", "z", "y", "z", "z", "y", "x"]
Y1 = ["", "z", "x", "y", "y", "z", "x", "z"]
X2 = ["", "M", "A", "E", "E", "E", "V", "A", "K", "L", "E", "K", "H", "L", "M", "L", "L", "R", "Q", "E", "Y", "V", "K", "L", "Q", "K", "K", "L", "A", "E", "T", "E", "K", "R", "C", "A", "L", "L", "A", "A", "Q", "A", "N", "K", "E", "S", "S", "S", "E", "S", "F", "I", "S", "R", "L", "L", "A", "I", "V", "A", "D"]
Y2 = ["", "M", "A", "E", "E", "E", "V", "A", "K", "L", "E", "K", "H", "L", "M", "L", "L", "R", "Q", "E", "Y", "V", "K", "L", "Q", "K", "K", "L", "A", "E", "T", "E", "K", "R", "C", "T", "L", "L", "A", "A", "Q", "A", "N", "K", "E", "N", "S", "N", "E", "S", "F", "I", "S", "R", "L", "L", "A", "I", "V", "A", "G"]


def longest_common_subsequence(X, Y):

    c = np.zeros((len(X), len(Y)))
    record = np.zeros((len(X), len(Y)))

    # 如果不等，比较上和左哪个大，
    for i in range(1, len(X)):
        for j in range(1, len(Y)):

            # 比较X,Y,若相等取左上+1,记录左上方
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
                record[i][j] = 1

            # 若不相等，则比较上和左哪个大
            else:

                # 如果上面大于等于左边，记录上边
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    record[i][j] = 2

                # 如果左边大于上面，记录左边
                else:
                    c[i][j] = c[i][j - 1]
                    record[i][j] = 0

    # 打印记录的值
    ans = []
    temp = []
    i = len(X) - 1
    j = len(Y) - 1
    y = 0
    while i > 0 and j > 0:
        if record[i][j] == 1:
            temp.append(X[i])
            i -= 1
            j -= 1
        elif record[i][j] == 2:
            i -= 1
        elif record[i][j] == 0:
            j -= 1

    for x in range(len(temp)-1, -1, -1):
        ans.append(temp[x])
        y += 1
    print("====================================================================")
    print(X)
    print(Y)
    print("最长公共子序列为：")
    print(ans)


longest_common_subsequence(X1, Y1)
longest_common_subsequence(X2, Y2)