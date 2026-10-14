"""
@Time ： 2026/9/17 15:18
@Auth ： seven
@File ：LA4.py
@IDE ：PyCharm
"""
import ast

def solve():
    matrix = ast.literal_eval(input().strip())
    str = input().strip()
    rows = len(matrix)
    cols = len(matrix[0])
    results = []
    if str == "row":
        for i in range(rows):
            temp = 0
            for j in range(cols):
                temp += matrix[i][j]
            results.append(float(temp / cols))
    else:
        for i in range(cols):
            temp = 0
            for j in range(rows):
                temp += matrix[j][i]
            results.append(float(temp / rows))
    print(results)

if __name__ == "__main__":
    solve()
