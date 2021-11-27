def is_isomorphic(s, t):
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == "__main__":
    tuple1 = ("bar", "foo")
    tuple2 = ("paper", "title")
    print(is_isomorphic(tuple1[0], tuple1[1]))
    print(is_isomorphic(tuple2[0], tuple2[1]))
