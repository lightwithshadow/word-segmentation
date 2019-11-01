import BMM
import FMM

words_dic = []


def init():
    with open('data/dic.txt', 'r', encoding='utf-8') as dic_input:
        for word in dic_input:
            words_dic.append(word.strip())
    return words_dic


def cut_words(raw_sentence, words_dic):
    bmm_word_list = BMM.cut_words(raw_sentence, words_dic)
    fmm_word_list = FMM.cut_words(raw_sentence, words_dic)
    bmm_word_list_size = len(bmm_word_list)
    fmm_word_list_size = len(fmm_word_list)
    if bmm_word_list_size != fmm_word_list_size:
        if bmm_word_list_size < fmm_word_list_size:
            return bmm_word_list
        else:
            return fmm_word_list
    else:
        FSingle = 0
        BSingle = 0
        isSame = True
        for i in range(len(fmm_word_list)):
            if fmm_word_list[i] not in bmm_word_list:
                isSame = False
            if len(fmm_word_list[i]) == 1:
                FSingle += 1
            if len(bmm_word_list[i]) == 1:
                BSingle += 1
        if isSame:
            return fmm_word_list
        elif BSingle > FSingle:
            return fmm_word_list
        else:
            return bmm_word_list


def main():
    init()
    while True:
        print('请输入待分词的序列：')
        input_str = input()
        if not input_str:
            break
        result = cut_words(input_str, words_dic)
        print('分词结果：')
        print(result)


if __name__ == '__main__':
    main()
