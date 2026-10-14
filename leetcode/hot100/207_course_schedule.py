"""
@Time ： 2026/10/13 17:04
@Auth ： seven
@File ：207_course_schedule.py
@IDE ：PyCharm
"""
#拓扑排序 + 入度 + 队列
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        n = len(prerequisites)
        indegree = [0] * numCourses
        for i in range(n):
            graph[prerequisites[i][0]].append(graph[prerequisites[i][1]])
            indegree[prerequisites[i][0]] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
            if not queue:
                return False
        return True








