from collections import deque

# 创建一个空的 deque
dq = deque()

# 从右边添加元素（类似 append）
dq.append('a')      # deque(['a'])
dq.append('b')      # deque(['a', 'b'])

print(dq[0])
print(dq[-1])
# 从左边添加元素
dq.appendleft('x')  # deque(['x', 'a', 'b'])

# 从右边删除元素
dq.pop()            # 返回 'b'，dq 变为 deque(['x', 'a'])

# 从左边删除元素
dq.popleft()        # 返回 'x'，dq 变为 deque(['a'])

print(dq)           # deque(['a'])


