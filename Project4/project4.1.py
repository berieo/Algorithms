value = 0
weight = 0
curV = 0
ans = None


def knapsack_01(i):
    global value, weight, curV, x, ans
    if i >= n:
        if value < curV:
            value = curV
            ans = x[:]
    else:
        if weight + w[i] <= c:
            x[i] = True
            weight += w[i]
            curV += v[i]
            knapsack_01(i + 1)
            weight -= w[i]
            curV -= v[i]
        x[i] = False
        knapsack_01(i + 1)


if __name__ == '__main__':
    n = 5
    c = 100
    w = [20, 30, 65, 40, 60]
    v = [10, 20, 30, 40, 50]
    x = [False for i in range(n)]
    knapsack_01(0)
    print(value)
    print(ans)