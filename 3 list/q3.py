def twonums_sum(n, lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == int(n):
                return (i, j)
    else:
        return "not found"


lst = [1, 4, 5, 6, 7, 8, 9, 10, \
        11, 12, 13, 14, 18, 19, \
        20, 21, 29, 34, 54, 65]
n = eval(input())
print(twonums_sum(n, lst))
