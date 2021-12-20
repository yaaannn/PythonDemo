import re


def fileReadOperate(filePath):
    file = open(filePath, "r", encoding="utf-8")
    text = file.read()
    file.close()
    return text


def fileWriteOperate(filePath, content):
    file = open(filePath, "w", encoding="utf-8")
    file.write(content)
    file.close()


def checkFilter(keywords, text):
    return re.sub("|".join(keywords), "*", text)


if __name__ == "__main__":
    text = fileReadOperate("9 file/article.txt")
    keywords = fileReadOperate("9 file/filtered_words.txt").split()
    keywords_list = list(keywords)
    fileWriteOperate("9 file/clean.txt", checkFilter(keywords_list, text))
