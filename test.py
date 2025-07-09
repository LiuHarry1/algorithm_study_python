from collections import deque

d = deque([1, 2, 3])
d.popleft()      # 返回 1
print(d)         # 输出 deque([2, 3])


print(d[-1])
d.append(5)
print(d)
d.pop()
print(d)