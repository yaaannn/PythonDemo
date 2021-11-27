import re

global str
str = input()


def count_len(n):
    count = 0
    word = re.split("[,| |.]", str)
    for i in word:
        if len(i) == n:
            count += 1
    return count


print(count_len(5))
print(count_len(4))
