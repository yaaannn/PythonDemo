def getText():
    txt = open("9 file/article.txt", "r", encoding='utf-8').read()
    txt = txt.lower()  #排除单词大小写影响
    for ch in ',.!?':
        txt = txt.replace(ch, " ")  #排除特殊字符及标点符号的影响
    return txt


if __name__ == "__main__":
    EnglishTxt = getText()
    words = EnglishTxt.split()
    print(max(words, key=len))
