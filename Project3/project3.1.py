"""

背包问题，要求考虑0/1背包问题和部分背包问题，采用贪心算法解决

"""

value = [20, 30, 65, 40, 60]
weight = [10, 20, 30, 40, 50]
value_weight = [(0,2), (1,1.5), (2,2.1), (3,1), (4,1.2)]
capacity = 100


def fractionl_knapsack(value, weight, value_weight, capacity):
    record = []
    sum = 0

    # 将性价比从高到低排序
    value_weight.sort(key=take_second, reverse=True)

    # 拿物品到背包中
    for x in range(0, len(value_weight)):

        # 如果重量超过最大背包数，则取部分
        if sum + weight[value_weight[x][0]] > capacity:
            record.append([value_weight[x][0], capacity - sum])
            break

        # 如果重量不大于最大背包书，则全部取
        else:
            sum = sum + weight[value_weight[x][0]]
            record.append([value_weight[x][0], weight[value_weight[x][0]]])

    print("部分背包问题：")
    for x in range(0, len(record)):
        print("从" + str(record[x][0]) + "号物品中取" + str(record[x][1]))
    print(record)


def knapsack_01(value, weight, value_weight, capacity):
    record = []
    sum = 0
    value_weight.sort(key=take_second, reverse=True)

    # 拿物品到背包中
    for x in range(0, len(value_weight)):

        # 如果重量超过最大背包数，则寻找可以放下的
        if sum + weight[value_weight[x][0]] > capacity:
            continue
            # record.append([value_weight[x][0], capacity - sum])
            # break

        # 如果重量不大于最大背包书，则全部取
        else:
            sum = sum + weight[value_weight[x][0]]
            record.append([value_weight[x][0], weight[value_weight[x][0]]])

    print("0/1背包问题：")
    for x in range(0, len(record)):
        print("从" + str(record[x][0]) + "号物品中取" + str(record[x][1]))
    print(record)

def take_second(elem):
    return elem[1]


fractionl_knapsack(value, weight, value_weight, capacity)
knapsack_01(value, weight, value_weight, capacity)