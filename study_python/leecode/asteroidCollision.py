def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        should_add = True  # 初始假设当前小行星需要入栈
        while stack and asteroid < 0 < stack[-1]:  # 可能发生碰撞
            if stack[-1] < -asteroid:  # 栈顶小行星被摧毁
                stack.pop()
            elif stack[-1] == -asteroid:  # 两者都被摧毁
                stack.pop()
                should_add = False  # 当前小行星不需要入栈
                break
            else:  # 当前小行星被摧毁
                should_add = False
                break
        if should_add:
            stack.append(asteroid)
    return stack