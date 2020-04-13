array1 = [1, 2, 3, 4, 5]
array2 = [1, 2, 2, 6, 7]
m = len(array1)
n = len(array2)
k = 5


def kth_of_array(array1, array2, m, n, k):
    mid1 = int(m / 2)
    mid2 = int(n / 2)

    # 记录最后一次调整是array1还是array2
    flag = 0
    while True:
        print(array1[mid1])
        print(array2[mid2])

        # 如果序列1的数大于等于序列2的，则将此时的序列记录下来与k做对比
        if array1[mid1] >= array2[mid2]:
            temp = m - mid1 + 1 + n - mid2
            flag = 1
        else:
            temp = m - mid1 + n - mid2 + 1
            flag = 2
        print(temp)
        # 如果此时序列等于k，则返回最后一次调整的值
        if temp == k:
            if flag == 1:
                return array1[mid1]
            elif flag == 2:
                return array2[mid2]

        # 如果此时序列大于k，对最后一次没有调整的序列二分
        elif temp > k:
            if flag == 1:
                if n - mid2 == 1:
                    mid2 += 1
                elif n == mid2:
                    if m - mid1 == 1:
                        mid1 += 1
                    else:
                        mid1 = int((n - mid1) / 2 + mid1)
                else:
                    mid2 = int((m - mid2) / 2 + mid2)
            elif flag == 2:
                if m - mid1 == 1:
                    mid1 += 1
                elif m == mid1:
                    if n - mid2 == 1:
                        mid2 += 1
                    else:
                        mid2 = int((m - mid2) / 2 + mid2)
                else:
                    mid1 = int((n - mid1) / 2 + mid1)

        # 如果此时序列小于k，对最后一次调整的序列二分
        elif temp < k:
            if flag == 1:
                if m == 1:
                    n -= 1
                else:
                    mid1 = int(mid1 - mid1 / 2)
            elif flag == 2:
                if n == 1:
                    m -= 1
                else:
                    mid2 = int(mid2 - mid2 / 2)


ans = kth_of_array(array1, array2, m - 1, n - 1, k)
print("第k个数是：")
print(ans)