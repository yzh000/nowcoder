"""
@Time ： 2026/9/17 13:34
@Auth ： seven
@File ：LA2.py
@IDE ：PyCharm
"""
#矩阵转置
import ast
import json
import sys
def solve():
    matrix = ast.literal_eval(input().strip())
    rows = len(matrix)
    cols = len(matrix[0])
    matrix_T = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            matrix_T[j][i] = matrix[i][j]

    print(json.dumps(matrix_T, separators=(',', ':')))
if __name__ == "__main__":
    solve()
