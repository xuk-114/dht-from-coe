# 1.处理技巧

### 1.列表排序:sort

#### 自定义排序

你可以通过传递 `key` 参数来自定义排序逻辑。`key` 参数应该是一个函数，该函数接受一个元素并返回一个用于排序的键。

###### 按长度排序

```
sort（key = len）
```

###### 多级排序

```python
data = [("apple", 3), ("banana", 2), ("cherry", 1)]
sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
print(sorted_data)  # 输出: [('cherry', 1), ('banana', 2), ('apple', 3)]
```

首先根据每个元组的第二个元素（索引为1）排序，如果这些值相同，则根据第一个元素（索引为0）排序

### 2.index

### 3.chr与ord

#### `ord()` 函数

作用：将一个字符转换为它的 ASCII 或 Unicode 编码（整数）。

用法：`ord(char)`

### `chr()` 函数

作用：将一个整数（ASCII 或 Unicode 编码）转换回字符。

用法：`chr(number)`

#### 问题解决：**凯撒密码**

代码实现

```python
def change(k,s):
    ans = []
    for char in s:
        if 'a' <= char <='z':
            change_char = chr((ord(char) -ord('a') -k) %26 +ord('a'))
        elif 'A' <=char <='Z':
            change_char = chr((ord(char) -ord('A') -k) %26 +ord('A'))
        else:
            change_char = char
        ans.append(change_char)
    return ''.join(ans)
```

### 4join

```python
words = ['Hello', 'world', 'Python']
result = ''.join(words)
```

### 5.bisect

列表的二分查找和插入

**bisect_left(list, x)**：返回 `x` 应该插入的位置，使得插入后列表仍然保持有序。如果列表中已经有 `x`，`bisect_left` 返回第一个 `x` 的位置。

**bisect_right(list, x)**：类似于 `bisect_left`，但返回 `x` 插入在已有 `x` 的后一个位置。

**insort_left(list, x)**：将 `x` 插入到列表中，使得 `x` 插入的位置是第一个符合要求的位置，确保有序。相当于先找到 `bisect_left` 的位置，再插入元素。

**insort_right(list, x)**：类似于 `insort_left`，但在已有 `x` 的最后一个位置之后插入。

### 6.可以确定方向：

使用

```
direct = [[0,1],[1,0],[0,-1],[-1,0]]
    if a[row+drow][col+dcol] != 0:
        x +=1
        drow,dcol = direct[x%4]
```

### 7.全排列函数

```
import itertools

result = list(itertools.product(range(2), repeat=6))
print(result)
```

product 笛卡尔积：类似于全排列

### 8.print(f"{num:.2f}")可以输出保留两位小数的num

### 9.for——else语句

```
for:
else:
```

`for ... else` 中的 `else` 仅在 `for` 循环没有被 `break` 提前终止时执行。

# 2.题目类型

### 1.贪心算法

局部最优到全局最优

#### 约束条件下地局部排序问题：

给定一个数组 `A` 和一个整数 `D`。

数组中的元素之间有某种可交换的条件（例如两个元素之间的差值不超过 `D`），满足该条件的元素可以交换位置。

目标是通过在符合条件的范围内交换元素，使得最终的数组在**字典序**上最小。

解法：

找出可以任意往前移动的数，存在一个组中，排序

```python
n,d = map(int,input().split())
h = [int(input()) for _ in range(n)]
num = []
inf = int(1e9)
used = [0] * n
for _ in range(n):
    minv,maxv = inf,-inf
    idx ,val = 0 ,inf
    for i in range(n):
        if used[i]:
            continue
        minv = min(minv,h[i])
        maxv = max(maxv,h[i])
        if (h[i] + d >= maxv and h[i] -d <= minv and h[i] <val):
            val =h[i]
            idx = i
    used[idx] =1
    print(h[idx])
```

#### 双指针：

对撞指针：数组中求两数之和

```python
def two_pointers(s,m):#s序列严格递增
    i = 0
    j =len(s)-1
    while i < j:
        if s[i] +s[j]==m:
            print(s[i],s[j])
            i += 1
            j -= 1
        elif s[i]+s[j] < m:
            i += 1
        else :
            j -= 1
```

#### 二分查找：

左边界left=0 右边界right=len -1

- - 计算中间位置 `mid`。
  
  - 如果中间位置的元素等于目标元素，返回其索引。
  
  - 如果中间位置的元素小于目标元素，调整左边界 `left` 为 `mid + 1`。
  
  - 如果中间位置的元素大于目标元素，调整右边界 `right` 为 `mid - 1`。
  
  - 重复上述步骤，直到找到目标元素或左边界超过右边界。
  
    

```
def binary_Search(arr,target): #arr严格单调增
    left,right= 0,len(arr) -1
    while left<= right :
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
        return -1

```

```
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

        # 将合并后的绳子长度重新插入堆中
        heapq.heappush(lengths, a + b)

    return total_cost
```

#### 最小绳子分割用堆来实现

### 2.DFS

#### 1.迷宫问题

##### 1.定义方向：eg：上下左右

```
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0, -1]
```

##### 2.辅助空间

标记当前位置是否访问

##### 3.终止条件：

##### 4.满足条件的操作

##### 5遍历与回溯：

```
def dfs(x, y):
    # 终止条件，例如超出边界或访问过
    if not is_valid(x, y):  
        return

    # 标记当前位置为已访问
    visited[x][y] = True

    # 如果满足某个条件（例如找到目标）
    if is_goal(x, y):
        # 可以进行计数、返回结果等操作
        result.append((x, y))
        return

    # 遍历所有可能的方向
    for i in range(4):  # 上、右、下、左
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny)

    # 如果需要回溯，可以在这里恢复状态
    visited[x][y] = False

```

### 3.BFS

当碰到岔道口时,总是先依次访问从该岔道口能直接到达的所有结点,然后再按这些结点被访问的顺序去依次访问它们能直接到达的所有结点，以此类推,直到所有结点都被访问为止

#### 模板

```
from collections import deque
  
def bfs(s, e):
    inq = set()
    inq.add(s)
      
    q = deque()
    q.append((0, s))

    while q:
        now, top = q.popleft() # 取出队首元素
        if top == e:
            return now # 返回需要的结果，如：步长、路径等信息

        # 将 top 的下一层结点中未曾入队的结点全部入队q，并加入集合inq设置为已入队
  
```

下面是对该模板中每一个步骤的说明,请结合代码一起看:

① 定义队列 q，并将起点(0, s)入队，0表示步长目前是0。 ② 写一个 while 循环，循环条件是队列q非空。 ③ 在 while 循环中，先取出队首元素 top。 ④ 将top 的下一层结点中所有**未曾入队**的结点入队，并标记它们的层号为 now 的层号加1，并加入集合inq设置为已入队。 ⑤ 返回 ② 继续循环。

为了防止走回头路，一般可以设置一个bool类型数组inq（即in queue的简写）来记录每个位置是否在BFS中已入过队。再强调一点，在BFS 中设置的 inq 数组的含义是判断结点是否已入过队，而不是**结点是否已被访问**。区别在于：如果设置成是否已被访问，有可能在某个结点正在队列中（但还未访问）时由于其他结点可以到达它而将这个结点再次入队，导致很多结点反复入队，计算量大大增加。因此BFS 中让每个结点只入队一次，故需要设置 inq 数组的含义为**结点是否已入过队**而非结点是否已被访问。

#### 重点在于约束条件

### 4.Dijkstra

计算从一个起始节点到所有其他节点的最短路径。该算法采用贪心策略，通过逐步选择距离起始节点最近的未访问节点并更新相邻节点的路径，直到找到所有节点的最短路径。

1.graph的作用储存与x相连的所有路线



```python
import heapq
def dijkstra(n,edges,s,t):
    graph = [[] for _ in range(n)]
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    pq = [(0,s)]
    visited = set()
    distances = [float('inf')] *n
    distances[s] = 0
    while pq:
        dist,node = heapq.heappop(pq)
        if node == t:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                new_dist = dist +weight
                if new_dist <distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq,(new_dist,neighbor))
    return -1
n,m,s,t = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(m)]
result =dijkstra(n,edges,s,t)
print(result)
```

### 5动态规划dp

重要的是画表格

**明确问题的状态和子问题**：

- 状态是指你需要做出选择的条件，比如当前的某个位置、剩余资源等。
- 子问题是指比原问题规模更小的问题，它们的解可以组合得到原问题的解。

**建立状态转移方程**：

- 这是动态规划的核心，表示如何通过子问题的解来构建当前问题的解。

**确定初始条件和边界情况**：

- 通常是问题最小规模时的解，例如数组长度为1时的结果。

**设计递推过程（或填表过程）**：

- 使用自底向上的方法解决问题，记录每个子问题的结果以避免重复计算。

**从记录的结果中构造答案**。

#### 1.0—1背包问题

它要求我们在容量有限的背包中装入物品，使得背包内物品的总价值最大化。每件物品只能选择要么装入，要么不装入，因此叫 **0-1背包**。

问题描述：

- 给定 n 件物品，每件物品有一个重量 w[i] 和一个价值 v[i]。
- 背包的容量是 C。
- 求背包中可以装入的最大价值。

解法

dpij表示前i个物品在背包容量j下的最大总价值

```
bag[i][j]=max(price[i]+bag[i-1][j-weight[i]], bag[i-1][j])
```

状态转移的方程：子问题：只考虑第i个放不放，则只和i-1有关，若第i个不放，为dpi-1 j

若i放则为第i的价格加dpi-1 j-i的重量

```
n, b = map(int, input().split())
price = [0] + [int(i) for i in input().split()]
weight = [0] + [int(i) for i in input().split()]

# 初始化一维 DP 数组
dp = [0] * (b + 1)

# 动态规划
for i in range(1, n + 1):
    # 逆序遍历容量，确保每个物品只能被使用一次
    for j in range(b, weight[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weight[i]] + price[i])

print(dp[b])
```



#### 2完全背包问题

只用一维的数组

**从小到大遍历**

```
n, a, b, c = map(int, input().split())
dp = [0]+[float('-inf')]*n

for i in range(1, n+1):
    for j in (a, b, c):
        if i >= j:
            dp[i] = max(dp[i-j] + 1, dp[i])

print(dp[n])
```

#### 3最长公共子序列

![image-20241221182051125](C:\Users\杜泓泰\AppData\Roaming\Typora\typora-user-images\image-20241221182051125.png)

#### 4多维dp

#### 5.整数划分

相当于把[j]省略

```
def integer_partition(n):
    # 初始化 DP 数组
    dp = [0] * (n + 1)
    dp[0] = 1  # 将 0 划分的方法只有一种：空集

    # 遍历所有可能的数字
    for j in range(1, n + 1):  # 当前可用的最大数字
        for i in range(j, n + 1):  # 遍历划分的目标数
            dp[i] += dp[i - j]
    
    return dp[n]

# 示例
n = 4
print(f"整数 {n} 的划分总数为: {integer_partition(n)}")  # 输出 5

```

<img src="C:\Users\杜泓泰\AppData\Roaming\Typora\typora-user-images\image-20241224231342763.png" alt="image-20241224231342763" style="zoom:66%;" />
