"""
@Time ： 2026/9/17 14:14
@Auth ： seven
@File ：LA3.py
@IDE ：PyCharm
"""
#重塑矩阵
import ast
import json


def solve():
    matrix = ast.literal_eval(input().strip())
    n = ast.literal_eval(input().strip())
    if not matrix or not n:
        print("-1")
        return
    rows = len(matrix)
    cols = len(matrix[0])
    cur_row = 0
    cur_col = 0
    results = []
    if rows * cols != n[0] * n[1]:
        print("-1")
        return
    for i in range(n[0]):
        temp = []
        for j in range(n[1]):
            if cur_col == cols and cur_row < rows:
                cur_row += 1
                cur_col = 0
            temp.append(matrix[cur_row][cur_col])
            cur_col += 1
        results.append(temp)
    print(results)

if __name__ == "__main__":
    solve()
