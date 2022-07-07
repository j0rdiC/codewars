# 4 kyu
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/python


rankings = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

dic = {key:value for key, value in zip(rankings, [n for n in range(len(rankings))])}


class User:

    def __init__(self):
        self.r = 0
        self.rank = rankings[self.r]
        self.progress = 0
    

    def inc_progress(self, rank):
        if rank == self.rank:
            self.progress += 3
        elif rank < self.rank:
            if dic[rank] - dic[self.rank] == -1:
                self.progress += 1
        else:
            d = dic[rank] - dic[self.rank]
            self.progress += 10 * d * d
        
        
        if self.progress >= 100:
            self.r += self.progress // 100
            self.rank = rankings[self.r]
            self.progress = self.progress % 100
        
        if self.rank == 8:
            self.progress = 0


u = User()

u.inc_progress(-5)
u.inc_progress(-7)


        

