def countchar(string):
    l = list('abcdefghijklmnopqrstuvwxyz')
    countList = []
    string = string.lower()
    for i in range(len(l)):
        countList.append(string.count(l[i]))
    return countList


string = input()
print(countchar(string))