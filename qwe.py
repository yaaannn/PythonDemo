def gen5(limit):

    val = 0

    while val < limit:

        yield val

        val += 5


for i in gen5(20):

    print(i, end='  ')