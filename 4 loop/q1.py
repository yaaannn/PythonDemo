def sum_of_square(num):
    str_num = str(num)
    sum = 0
    for i in range(len(str_num)):
        sum += int(str_num[i])**2
    return sum


def find_happy_number(num, count, list_num):
    sum1 = sum_of_square(num)
    if count == 0:
        list_num.append(num)
    if sum1 == 1:
        return True
    else:
        count += 1
        if count < 10:
            return find_happy_number(sum1, count, list_num)
        else:
            list_num.pop()
            return False


if __name__ == "__main__":
    count = 0
    list_num = []
    for i in range(100):
        find_happy_number(i, count, list_num)
        if len(list_num) == 10:
            break
    print(list_num)
