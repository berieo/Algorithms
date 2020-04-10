"""

Priority: First in, Largest out.
采用堆排序来实现这样的特点

"""


class HeapSort:
    def __init__(self, queue, size):
        self.queue = queue
        self.size = size
        self.index = 0

    def add(self, item):
        self.size += 1
        self.queue.append(item)
        self.add_adjustment()

    def delete(self):
        self.delete_adjustment()
        self.size -= 1

    def init(self):

        # 检查是否有左叶子节点
        while self.index * 2 + 1 < self.size:

            # 如果左叶子节点比该节点小，则替换
            if self.queue[self.index] < self.queue[self.index * 2 + 1]:
                temp = self.queue[self.index]
                self.queue[self.index] = self.queue[self.index * 2 + 1]
                self.queue[self.index * 2 + 1] = temp

            # 检查是否有右叶子节点，若有则检查是否比右叶子节点小，若小则替换
            if self.index * 2 + 2 < self.size and self.queue[self.index] < self.queue[self.index * 2 + 2]:
                temp = self.queue[self.index]
                self.queue[self.index] = self.queue[self.index * 2 + 2]
                self.queue[self.index * 2 + 2] = temp
            self.index += 1

    # 添加一个元素后，堆排序做调整
    def add_adjustment(self):
        i = self.size - 1

        # 采用上升的方法，将添加的元素与父母节点作比较，逐渐改为大顶堆
        while int(i / 2) >= 0:
            if self.queue[int((i - 1) / 2)] < self.queue[i]:
                temp = self.queue[i]
                self.queue[i] = self.queue[int((i - 1) / 2)]
                self.queue[int((i - 1) / 2)] = temp
                i = int((i - 1) / 2)
            else:
                self.index += 1
                break

    # 删除一个元素后，堆排序做调整
    def delete_adjustment(self):
        i = 0

        # 记录最后一次替换是左边还是右边
        flag = -1

        # 采用下降的方法
        while (i * 2 + 1) < self.size:

            # 如果左叶子比右叶子节点大，则替换
            if self.queue[i * 2 + 1] >= self.queue[i * 2 + 2]:
                temp = self.queue[i]
                self.queue[i] = self.queue[i * 2 + 1]
                self.queue[i * 2 + 1] = temp
                i = i * 2 + 1
                flag = 0

            # 如果右叶子节点存在，并且右叶子节点比左叶子节点大，则替换
            if i * 2 + 2 < self.size and self.queue[i * 2 + 1] < self.queue[i * 2 + 2]:
                temp = self.queue[i]
                self.queue[i] = self.queue[i * 2 + 2]
                self.queue[i * 2 + 2] = temp
                i = i * 2 + 2
                flag = 1

        # 将最后一次替换的元素pop出数组
        if i < self.size:
            self.queue.pop(i)


class PriorityQueue:
    # 对优先级队列初始化
    def __init__(self, HeapSort):
        self.heapsort = HeapSort
        heapsort.init()

    # 入列，调用堆排序的add方法
    def push(self, item):
        self.heapsort.add(item)

    # 出列，调用堆排序的delete方法
    def pop(self):
        self.heapsort.delete()


queue = [1, 5, 2, 4]

# 声明一个HeapSort对象传入PriorityQueue中
heapsort = HeapSort(queue, len(queue))
priorityqueue = PriorityQueue(heapsort)

# 声明PriorityQueue对象时会将堆排序初始化
print("初始化结果：")
print(queue)

# 优先级队列中添加一个元素
priorityqueue.push(6)
print("添加一个元素：")
print(queue)

# 优先级队列中出列一个元素
priorityqueue.pop()
print("出列一个元素：")
print(queue)




