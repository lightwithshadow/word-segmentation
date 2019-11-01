# words_dic = []
#
#
# def init():
#     """
#     读取词典文件
#     :return:
#     """
#     with open('data/dic.txt', 'r', encoding='utf-8') as dic_input:
#         for word in dic_input:
#             words_dic.append(word.strip())
#     return words_dic
#  test

def cut_words(raw_sentence, words_dic):
    # 统计词典中词的最大长度
    max_length = max(len(word) for word in words_dic)
    sentence = raw_sentence.strip()
    words_length = len(sentence)
    # 存储切分好的词
    cut_word_list = []
    while words_length > 0:
        max_cut_length = min(max_length, words_length)
        subsentence = sentence[-max_cut_length:]
        while max_cut_length > 0:
            if subsentence in words_dic:
                cut_word_list.append(subsentence)
                break
            elif max_cut_length == 1:
                cut_word_list.append(subsentence)
                break
            else:
                max_cut_length = max_cut_length - 1
                subsentence = subsentence[-max_cut_length:]
        sentence = sentence[0: -max_cut_length]
        words_length = words_length - max_cut_length
    cut_word_list.reverse()
    # words = '/'.join(cut_word_list)
    # return words
    return cut_word_list



# def main():
#     '''
#     交互函数
#     :return:
#     '''
#     init()
#     while True:
#         print('请输入待分词的序列：')
#         input_str = input()
#         if not input_str:
#             break
#         result = cut_words(input_str, words_dic)
#         print('分词结果：')
#         print(result)
#
#
# if __name__ == '__main__':
#     main()
