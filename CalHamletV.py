#CalHamletV.py 文本词频
# def getText():
#     tex = open("hamlet.txt", "r").read()
#     tex = tex.lower()
#     for ch in '!"#$%^&*()+,;:<>=_@~' :
#         tex = tex.replace(ch, " ")
#     return tex
#
# hamletTex = getText()
# words = hamletTex.split()
# counts = {}
# for word in  words:
#     counts[word] = counts.get(word, 0) + 1
# items = list(counts.items())
# items.sort(key=lambda x:x[1], reverse=True)
# for i in range(10):
#     word, count = items[i]
#     print("{0:<10}{1:>5}".format(word, count))

# 中文分词
import jieba
txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人", "不可", "军马",
            "引兵", "不能", "如此", "军士", "左右", "商议",
            "主公", "如何", "次日", "大喜", "天下", "东吴",
            "于是", "今日", "不敢", "魏兵", "陛下", "一人"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or  word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in  excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

