"""

最大子数组问题，可以采用暴力枚举，优化枚举，分而治之，动态规划等方法，其中动态规划的方法算法复杂度为O(n)

"""
import copy

a = [0, -2, 11, -4, 13, -5, -2]
X1 = [0, -1, -3, 3, 5, -4, 3, 2, -2, 3, 6]
X2 = [0, 1, -2, 4, 5, -2, 8, 3, -2, 6, 3, 7, -1]


def max_sum(X):
    D = copy.copy(X)
    Rec = copy.copy(X)
    Rec[len(Rec)-1] = len(Rec) - 1
    # 从右至左计算以i开头的最大子数组
    for i in range(len(X)-2, 0, -1):
        if D[i + 1] > 0:
            D[i] = X[i] + D[i+1]
            Rec[i] = Rec[i+1]
        elif D[i + 1] <= 0:
            D[i] = X[i]
            Rec[i] = i

    # 选出D中最大的子数组
    start = D.index(max(D))
    end = Rec[start]
    ans = X[start:end+1]
    print("最大子数组为：")
    print(ans)

    # 最大子数组和
    print("最大子数组和为：")
    print(sum(ans))


max_sum(a)
