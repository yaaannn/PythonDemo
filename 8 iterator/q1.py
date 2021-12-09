from itertools import count


def getPalindrome():
    yield 0
    for digits in count(1):
        first = 10**((digits - 1) // 2)
        for s in map(str, range(first, 10 * first)):
            yield int(s + s[-(digits % 2) - 1::-1])


def allPalindromes():
    palindromGenerator = getPalindrome()
    palindromeList = []
    for palindrome in palindromGenerator:
        if palindrome > 10000:
            break
        if palindrome < 1:
            continue
        palindromeList.append(palindrome)
    return palindromeList


if __name__ == "__main__":
    print(allPalindromes())