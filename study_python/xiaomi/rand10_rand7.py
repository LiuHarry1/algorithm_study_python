


"""
你已经有了一个可以等概率生成 1 到 7 之间整数的函数 rand7()，请用它来实现一个新的函数 rand10()，使其能等概率地生成 1 到 10 之间的整数。


 Step 2: 拒绝采样
如果 num <= 40，我们就接受

然后用 (num % 10) + 1 得到 1~10 等概率的结果

如果 num > 40，我们就丢弃它，重新采样

这样我们就得到了完美均匀的 rand10()！




"""

def rand10():
    while True:
        row = rand7()
        col = rand7()
        num = (row - 1) * 7 + col  # Uniformly random in [1, 49]
        if num <= 40:
            return 1 + (num - 1) % 10
