def inDict(word):
    result = ''
    fr = open('fruits.txt', 'r', encoding='utf-8')
    keys = []  # 用来存储读取的顺序
    dic = {}
    for line in fr:
        line = line.replace("\n", '')
        v = line.split(':')
        dic[v[0]] = v[1]
        keys.append(v[0])
    if word in keys:
        result = dic[word]
        print("find!")
    else:
        return ''
    fr.close()
    return result


def addToDic(word, word1):
    with open("fruits.txt", encoding="utf-8", mode="a") as file:
        file.write(word + ':' + word1 + '\n')
    file.close()


def main():
    while True:
        word = input("Input an English word: ")
        result = inDict(word)
        if result != '':
            print(word, result)
        else:
            word1 = input("Not Found!Input the Chinese:")
            addToDic(word, word1)
        op = input("Wanna Continue?(Y/N): ")
        if op in ('Y', 'y'):
            continue
        elif op in ('N', 'n'):
            break
        else:
            break


if __name__ == '__main__':
    main()