"""

调度问题，需要平均完成时间最小，采用贪心算法的思路

"""

time = [(1, 15), (2, 8), (3, 3), (4, 10)]


def scheduling_problem(time):
    # 按照从小到大排序
    time.sort(key=take_second)
    ans = 0
    value = []
    order = []
    for i in range(0, len(time)):
        value.append(time[i][1])
        ans = sum(value) + ans
    ans = ans / len(value)
    print("最小平均时间为：")
    print(ans)
    print("执行顺序为：")
    for i in time:
        order.append(i[0])
    print(order)


def take_second(elem):
    return elem[1]


scheduling_problem(time)