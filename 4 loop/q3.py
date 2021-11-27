from math import sqrt


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_monisen(n):
    if n == 1:
        return 2, 3
    p = 2
    count = 0
    while True:
        if is_prime(p):
            m = 2**p - 1
            if is_prime(m):
                count += 1
                if count == n:
                    return p, m
        p += 1


if __name__ == "__main__":
    n = eval(input())
    print(f"p={find_monisen(n)[0]} m={find_monisen(n)[1]}")
