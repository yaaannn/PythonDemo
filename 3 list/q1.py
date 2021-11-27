def isArithmetic(l):
    l.sort()
    # print(l)
    if (len(l) == 2):
        return True
    for i in range(1, len(l) - 2):
        if (l[i + 1] - l[i] == l[i + 2] - l[i + 1]):
            return True
        else:
            return False


l = list(map(int, input().split()))
print(isArithmetic(l))
