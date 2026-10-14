"""
@Time ： 2026/9/17 13:13
@Auth ： seven
@File ：LA1.py
@IDE ：PyCharm
"""
#矩阵与向量乘法
import ast
def solve():
    matrix = ast.literal_eval(input().strip())
    vector = ast.literal_eval(input().strip())

    if not matrix:
        print(-1)
        return

    for row in matrix:
        if len(row) != len(vector):
            print(-1)
            return

    result = []

    for row in matrix:
        total = 0
        for i in range(len(row)):
            total += row[i] * vector[i]
        result.append(total)

    print(result)

if __name__ == "__main__":
    solve()
