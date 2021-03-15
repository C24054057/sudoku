import time

class Neighborhood():
    def __init__(self):
        self.r = -1
        self.c = -1

    def FindRowNeighbors(self):
        return [(self.r, i) for i in range(1, 10)]

    def FindColNeighbors(self):
        return [(i, self.c) for i in range(1, 10)]

    def FindBlockNeighbors(self):
        if self.r <= 3:
            ir = [1, 2, 3]
        elif self.r >= 7:
            ir = [7, 8, 9]
        else:
            ir = [4, 5, 6]
        if self.c <= 3:
            ic = [1, 2, 3]
        elif self.c >= 7:
            ic = [7, 8, 9]
        else:
            ic = [4, 5, 6]
        bnbs = list()
        for iir in ir:
            for iic in ic:
                bnbs.append((iir, iic))
        return bnbs
        
    def FindNeighbors(self):
        # 回傳一個包含所有鄰居的list
        nbs = list()
        nbs += self.FindRowNeighbors()
        nbs += self.FindColNeighbors()
        nbs += self.FindBlockNeighbors()
        return(nbs)
  
class Sudoku(Neighborhood):
    def __init__(self, inp):
        super().__init__()
        self.inp = inp
        self.start_time = time.time()

    def Print(self):
        # 印出目前的數獨
        time.sleep(0.0000001)
        for pos, n in self.inp.items():
            print(n, end=' ')
            if pos[1] == 9:
               print()
        print()

    def Solve(self):
        # 印出數獨
        self.Print()
        # 找出第一個0的位置
        for pos, n in self.inp.items():
            if n == 0:
                self.r, self.c = pos
                break
        # 找不到數字是0的位置，代表數獨完成了
        if self.r == -1 and self.c == -1:
            print("完成了")
            print("花了{:.2}秒".format(time.time()-self.start_time))
            exit() # 終止程式(剛好可以離開遞迴)
        # 判斷可以輸入哪幾個數字
        nbs = self.FindNeighbors()
        candidates = [i for i in range(1, 10)]
        for pos in nbs:
            if self.inp[pos] == 0 or self.inp[pos] not in candidates:
                continue
            candidates.remove(self.inp[pos])
        try_pos_of_r, try_pos_of_c =  self.r, self.c # 為了保存數獨目前位置的座標，而用兩個變數儲存
        self.r, self.c = -1, -1
        # 如果沒有可以輸入的數字 -> 離開solve函式
        if not candidates:
            return
        # 進入新的solve函式
        for cand in candidates:
            self.inp[(try_pos_of_r, try_pos_of_c)] = cand
            self.Solve()
        # 所有候選人數字都試過，代表無解 -> 離開solve函式
        self.inp[(try_pos_of_r, try_pos_of_c)] = 0 # 把目前位置的數字還原
        return



    