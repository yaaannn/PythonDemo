def fun(n):
    if n == 1:
        print("1*3+1=4")
        print("4/2=2")
        print("2/2=1")

    while n != 1:
        if n % 2 == 0:
            a1 = n / 2
            print(f"{n:.0f}/2={a1:.0f}")
            n = a1
        else:
            a2 = n * 3 + 1
            print(f"{n:.0f}*3+1={a2:.0f}")
            n = a2


if __name__ == "__main__":
    n = eval(input())
    fun(n)