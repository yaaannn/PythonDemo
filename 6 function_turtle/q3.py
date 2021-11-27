def func(lst):
    if all(i == 0 for i in lst):
        return '0'

    return ''.join(
        sorted((str(i) for i in lst),
               reverse=False,
               key=lambda i: i * (len(str(min(lst))) * 2 // len(i))))


if __name__ == "__main__":
    lst = [3, 40, 41, 43, 74, 9]
    print(func(lst))