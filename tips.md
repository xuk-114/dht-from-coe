# 1.字符串变为列表：

​	`a = list(map(int,input()))`

# 2.浮点数的精确

​	math.isclose函数：

```
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
```

### 参数

- `a`: 第一个浮点数。
- `b`: 第二个浮点数。
- `rel_tol` (可选): 相对容差，即允许的最大相对误差，默认值为 `1e-09`。
- `abs_tol` (可选): 绝对容差，即允许的最大绝对误差，默认值为 `0.0`。

### 返回值

- 如果两个数在给定的容差范围内，则返回 `True`。
- 否则返回 `False`。

# 3.无穷的表示

```
positive_infinity = float('inf')
negative_infinity = float('-inf')
```

# 4.字符串replace

```
str.replace(old, new[, count])
```

### 参数

- `old`：要被替换的子字符串。
- `new`：用于替换 `old` 的新子字符串。
- `count`（可选）：指定替换的最大次数。如果不提供此参数，则所有匹配的子字符串都将被替换。

### 返回值

返回一个新的字符串，其中指定的子字符串被替换为新的子字符串。原始字符串不会被修改。

# 5.质数的判断

1.检查从2到该数的平方根之间的所有数是否能整除该数

##### 2.优化试除法 通过减少需要检查的数的数量来优化基本试除法：

1. **2 是唯一的偶数质数**：
   - 2 是最小的质数，也是唯一的偶数质数。
   - 除了2之外，所有的偶数都可以被2整除，因此它们都不是质数。
2. **奇数的性质**：
   - 所有大于2的质数都是奇数。
   - 因此，我们只需要检查奇数，而不需要检查偶数（除了2）。

# 6.查找列表、元组或字符串中某个元素

1.字符串的 `.index()` 方法

```
str.index(sub, start, end)
```

#### 参数

- `sub`：要查找的子字符串。
- `start`（可选）：开始查找的索引位置，默认为0。
- `end`（可选）：结束查找的索引位置，默认为字符串的长度。

#### 返回值

返回 `sub` 在字符串中第一次出现的索引位置。如果找不到 `sub`，则引发 `ValueError`

2列表的 `.index()` 方法

```
list.index(element, start, end)
```

#### 参数

- `element`：要查找的元素。
- `start`（可选）：开始查找的索引位置，默认为0。
- `end`（可选）：结束查找的索引位置，默认为列表的长度。

7.