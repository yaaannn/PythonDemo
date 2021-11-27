def fun(n):
    temp0 = []
    temp1 = []
    for i in range(101):
        temp0.append(i)
        if i // 10 == n or i % 10 == n or i % n == 0:
            temp1.append(i)
    return list(set(temp0) - set(temp1))


if __name__ == "__main__":
    n = eval(input())
    count = 0
    s1 = ""
    num_list = fun(n)
    for i in range(len(num_list)):
        print(num_list[i], end=",")
        count += 1
        if count % 10 == 0:
            print("\n", end="")
