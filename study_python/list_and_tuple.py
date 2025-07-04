# List 可修改
a = [1, 2, 3]
a[0] = 100  # OK

# Tuple 不可修改
b = (1, 2, 3)
b[0] = 100  # ❌ 报错：TypeError

