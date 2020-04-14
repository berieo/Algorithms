"""

矩阵链乘问题要求元素相乘的总次数最少，采用动态规划的思路解决

"""

a = [3, 5, 2, 1, 10]
b = [2, 7, 3, 6, 10]
c = [10, 3, 15, 12, 7, 2]
d = [7, 2, 4, 15, 20, 5]
record = []


def matrix_chain(array):
    size = len(array)
    # 最小值设为无穷大
    minimum = 999999999999
    cost = 0

    # 如果长度为3的话，可以直接计算
    if len(array) == 3:
        return array[0] * array[1] * array[2]

    # 对左边进行划分
    for i in range(2, size - 1):

        # 将左右数组分开
        left = array[0:i+1]
        right = array[i:]

        # 计算需要乘的次数
        if len(left) == 2:
            cost = array[0] * array[1] * array[size - 1] + matrix_chain(right)

        elif len(right) == 2:
            cost = matrix_chain(left) + array[0] * array[size - 2] * array[size - 1]

        else:
            cost = matrix_chain(left) + matrix_chain(right) + array[0] * array[i] * array[size - 1]

        if cost < minimum :
            minimum = cost
        record.append(minimum)

    # return minimum

    # 对右边进行划分
    for i in range(2, size - 1):
        left = array[0:size-i]
        right = array[size-i-1:size]

        # 计算需要乘的次数
        if len(left) == 2:
            cost = array[0] * array[1] * array[size - 1] + matrix_chain(right)

        elif len(right) == 2:
            cost = matrix_chain(left) + array[0] * array[size - 2] * array[size - 1]

        else:
            cost = matrix_chain(left) + matrix_chain(right) + array[0] * array[size - i - 1] * array[size - 1]

        if cost < minimum:
            minimum = cost
        record.append(minimum)

    return minimum


print("a矩阵链乘最小次数为：")
matrix_chain(a)
print(record[-1])
print("b矩阵链乘最小次数为：")
matrix_chain(b)
print(record[-1])
print("c矩阵链乘最小次数为：")
matrix_chain(c)
print(record[-1])
print("d矩阵链乘最小次数为：")
matrix_chain(d)
print(record[-1])