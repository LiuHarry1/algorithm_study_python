from collections import deque

def canFinish(numCourses, prerequisites):
    """
      :type numCourses: int
      :type prerequisites: List[List[int]]
      :rtype: bool
      """
    # 初始化入度表和邻接表
    in_degree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]

    # 构建图
    for course, pre in prerequisites:
        adj[pre].append(course)  # pre -> course
        in_degree[course] += 1

    # 初始化队列（入度为0的节点）
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    # 拓扑排序
    visited = 0
    while queue:
        current = queue.popleft()
        visited += 1
        for neighbor in adj[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == numCourses


if __name__ == '__main__':

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(canFinish(numCourses, prerequisites))  # 输出: True