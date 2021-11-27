def fun(str):
    word, number, other = 0, 0, 0
    for i in str:
        if i.isalpha():
            word += 1
        elif i.isdigit():
            number += 1
        else:
            other += 1
    return word, number, other


str = input()
print(fun(str))