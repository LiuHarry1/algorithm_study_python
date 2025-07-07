import random


def flip_coin():
    """模拟抛硬币，返回0或1，概率均等"""
    return random.randint(0, 1)


def roll_dice():
    while True:
        # 用三次抛硬币生成一个 0 到 7 的数字
        bits = [flip_coin() for _ in range(3)]
        num = bits[0] * 4 + bits[1] * 2 + bits[2]

        print(num)
        if num < 6:
            return num + 1  # 转换为骰子点数 1~6
        # 否则重试

# 测试一下掷 10 次骰子
for _ in range(10):
    print(roll_dice())
