class Fibs:
    def __init__(self, n):
        self.n, self.pnum, self.nnum = n, 0, 1

    def __next__(self):
        if self.pnum < self.n:
            num = self.pnum
            self.pnum, self.nnum = self.nnum, self.pnum + self.nnum
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    fibs = Fibs(1000)
    for i in fibs:
        print(i, end=" ")
