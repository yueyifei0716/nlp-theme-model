# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def read_csv_column(csv_path, column_name):
    df = pd.read_csv(csv_path, encoding='utf-8', low_memory=False)
    return df[column_name].astype(str)


def split_sentence(column_contents):
    for i in range(len(column_contents)):
        column_contents[i] = column_contents[i].split()


def txt_to_list(txt_path):
    f = open(txt_path, 'r+')
    content = f.read()
    f.close()
    words = [content]
    return words


if __name__ == "__main__":
    contents = read_csv_column('./dataset/trump1.csv', '微博正文')
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(contents))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()

    # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    for i in range(len(weight)):
        result_dict = dict(zip(word, weight[i]))
        result_list = sorted(result_dict.items(), key=lambda kv: kv[1], reverse=True)
        result_list = result_list[:20]
        print("----------------------")
        for item in result_list:
            print(item)
        # for j in range(len(word)):
        #
        #     print(word[j], weight[i][j])
