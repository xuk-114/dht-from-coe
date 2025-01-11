import heapq


def min_cut_cost(lengths):
    # 初始化最小堆
    heapq.heapify(lengths)
    total_cost = 0

    # 当堆中元素多于1时继续切割
    while len(lengths) > 1:
        # 取出最短的两段绳子
        a = heapq.heappop(lengths)
        b = heapq.heappop(lengths)

        # 当前切割的开销
        cost = a + b
        total_cost += cost

        # 新的绳段加入堆中
        heapq.heappush(lengths, cost)

    return total_cost
n = int(input())
s = list(map(int,input().split()))
print(min_cut_cost(s))