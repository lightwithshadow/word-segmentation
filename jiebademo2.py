import jieba


words = jieba.cut('大鹏主演的屌丝男士上了微博热搜')
print('/'.join(words))


# 加载自定义词典
jieba.load_userdict('user_dict.txt')
words = jieba.cut('大鹏主演的屌丝男士上了微博热搜')
print('/'.join(words))

