import jieba


# 精确模式
words = jieba.cut('我毕业后，就职于中科院自动化所。')
print('采用精确模式：')
print('/'.join(words))


words = jieba.cut('我毕业后，就职于中科院自动化所。', cut_all=True)
print('采用全模式：')
print('/'.join(words))


# 使用搜索引擎模式
words = jieba.cut_for_search('我毕业后，就职于中科院自动化所。')
print('采用搜索引擎模式：')
print('/'.join(words))
