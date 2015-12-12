from collections import defaultdict
from stopwords import STOPWORDS


while True:
    question = raw_input('Paste Question Here:\n').lower().split()
    answer = raw_input('Paste Answer Here:\n').lower().split()

    question_dict = defaultdict(int)
    answer_dict = defaultdict(int)


    for word in question:
        if word in STOPWORDS:
            continue
        question_dict[word] += 1

    for word in answer:
        if word in STOPWORDS:
            continue
        answer_dict[word] += 1


    question_words_set = set(question_dict.keys())
    answer_word_set =  set(answer_dict.keys())

    overlap = question_words_set.intersection(answer_word_set)

    for word in overlap:
        print "{}\t\tQuestion: {} Answer {}".format(word, question_dict[word], answer_dict[word])



