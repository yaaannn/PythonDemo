def reverseVowels(s):
    sStr = list(s)
    voList = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    front = 0
    length = len(sStr)
    back = length - 1
    while front < back:
        while front < length and sStr[front] not in voList:
            front += 1
        while back >= 0 and sStr[back] not in voList:
            back -= 1
        if front < back:
            sStr[front], sStr[back] = sStr[back], sStr[front]
            front += 1
            back -= 1
    return "".join(sStr)


str = input()
print(reverseVowels(str))