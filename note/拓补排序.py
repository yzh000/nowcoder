"""
@Time ： 2026/10/13 17:06
@Auth ： seven
@File ：拓补排序.py
@IDE ：PyCharm
"""
from collections import deque

def topological_sort(n, edges):
    # 1. 建图
    gragh = [[] for _ in range(n)]

    # 2. 入度数组
    indegree = [0] * n

    for cur, pre in edges:
        gragh[pre].append(cur)
        indegree[cur] += 1

    # 3. 所有入度为 0 的节点进入队列
    queue = deque()

    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
    # 记录拓扑序
    order = []
    # 4. BFS
    while queue:
        node = queue.popleft()
        order.append(node)

        # 5. 删除 node 对后续节点的依赖
        for next_node in gragh[node]:
            indegree[next_node] -= 1
            # 6. 前置条件全部完成
            if indegree[next_node] == 0:
                queue.append(next_node)

    return order