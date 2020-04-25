import sys
import re


def preprocess():
    count = 0
    data = open(sys.argv[1], "rb").readlines()
    data = data[:7970]
    for i in data:
        count += 1
        d = i.split()
        # print(" ".join([i.decode('utf-8') for i in d[8:]]))
        with open("preprocessed_data.txt", "a", encoding="utf-8") as f:
            line = " ".join([i.decode('utf-8') for i in d[8:]])
            line = re.sub(r'^\+*\$\+* ', "", line)
            if 2 <= len(line.split()) <= 25:
                f.write(line + "\n")


def afterPreprocess():
    data = open("preprocessed_data.txt").readlines()
    short_data = []
    for line in data:
        if 2 <= len(line.split()) <= 25:
            short_data.append(line)
    word2count = {}
    totalWord = 0

    for text in short_data:
        for word in text.split():
            if word not in word2count:
                word2count[word] = 1
            else:
                word2count[word] += 1
            totalWord += 1

    print("word count :", totalWord)

    wordMoreThanFifteenTiems = []
    threshold = 15
    for word, count in word2count.items():
        if count >= threshold and len(word) > 1:
            wordMoreThanFifteenTiems.append(word)

    data_15 = []
    for line in short_data:
        str1 = ""
        for word in line.split():
            if word in wordMoreThanFifteenTiems:
                str1 = " ".join((str1, word))
        data_15.append(str1)

    short_data_consize = []
    for line in data_15:
        if 3 <= len(line.split()) <= 15:
            print(line)
            short_data_consize.append(line)
        else:
            None

    with open("tokenFile.txt", "a") as f:
        for line in short_data_consize:
            f.write(line)


def printBeg():
    data = open("preprocessed_data.txt").readlines()
    for line in data:
        # print(re.findall(r'^\+*\$\+*', line))
        print(re.sub(r'^\+*\$\+* ', "", line))


if __name__ == "__main__":
    # preprocess()
    # printBeg()
    afterPreprocess()
