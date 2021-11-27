def reverse_string(str):
    if len(str) <= 1:
        return str
    else:
        return reverse_string(str[1:]) + str[0]


if __name__ == "__main__":
    str = "abcdef"
    print(reverse_string(str))