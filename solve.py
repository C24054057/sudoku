import time
from sudoku import Sudoku

'''
此程式用來解.txt的數獨題目
'''

#從.txt輸入數獨的問題
with open('input.txt', 'r') as f:
    inp = dict()
    r, c = 1, 1
    for line in f.readlines():
        for num in line.split(' '):
            inp[(r, c)] = int(num.strip())
            c += 1
        c = 1
        r += 1

if __name__ == '__main__':
    s = Sudoku(inp)
    s.Solve()
    