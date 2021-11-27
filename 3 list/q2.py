import re


def splitList(l):
    # nl = []
    temp = []
    split_list = []
    for i in range(1, len(l)):
        if i < len(l) - 1:
            if (l[i] != l[i + 1]):
                temp.append(i + 1)
    temp.append(len(l))
    for j in range(len(temp)):
        if j == 0:
            split_list.append(l[:temp[j]])
        else:
            split_list.append(l[temp[j - 1]:temp[j]])
    return split_list


# l = [0, 0, 0, 1, 1, 2, 3, 3, 3, 2, 3, 3, 0, 0]

str = input()
l = re.split("[|,|[|]|]", str)
while "" in l:
    l.remove("")
l = list(map(int, l))
print(splitList(l))