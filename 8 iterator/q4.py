class inclusive_range:
    def __init__(self, start, stop, step) -> None:
        self.start = start - step
        self.stop = stop + step
        self.step = step

    def __next__(self):

        self.cur_val += self.step
        if self.cur_val < self.stop:
            return self.cur_val
        else:
            raise StopIteration

    def __iter__(self):
        self.cur_val = self.start
        return self


if __name__ == "__main__":
    for i in inclusive_range(2, 10, 2):
        print(i, end=" ")
