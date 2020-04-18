"""

八皇后问题，采用回溯算法的思路解决

"""


def eight_queen(record, i):

    # 如果已经遍历完所有行数，则打印记录值
    if i == len(record):
        print(record)
        return

    # 检查每一列是否有重提
    for j in range(8):
        flag = 1
        for x in range(i):

            # 检查是否在同一列或者同一斜线上，斜线可能是左斜线或者右斜线，所以要加abs()
            if record[x][1] == j or i - record[x][0] == abs(j - record[x][1]):
                flag = 0
                break

        # 如果没有冲突则继续递归
        if flag == 1:
            record[i] = [i, j]
            eight_queen(record, i + 1)


eight_queen([[-1] * 2] * 8, 0)