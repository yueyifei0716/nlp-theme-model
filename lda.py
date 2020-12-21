# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd


def txt_to_list(txt_path):
    f = open(txt_path, 'r+')
    content = f.read()
    f.close()
    list = []
    list.append(content)
    return list


def print_top_words(model, feature_names, n_top_words):
    # 打印每个主题下权重较高的term
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    # 打印主题-词语分布矩阵
    print(model.components_)


if __name__ == "__main__":
    trump1 = txt_to_list('/Users/yueyifei/Code/python_test/NLP/theme_model/trump3.txt')
    tf_vectorizer = CountVectorizer()
    tf = tf_vectorizer.fit_transform(trump1)

    n_topics = 10

    while n_topics <= 100:

        n_top_words = 20

        lda = LatentDirichletAllocation(n_components=n_topics, max_iter=50,
                                        learning_method='online',
                                        learning_offset=50.,
                                        random_state=0)
        lda.fit(tf)
        feature_names = tf_vectorizer.get_feature_names()
        compoments = lda.components_

        # docres = lda.fit_transform(tf)

        topic_dic = {}
        for no in range(n_topics):
            topic = ([feature_names[i] for i in compoments[no].argsort()[:-n_top_words - 1:-1]])
            topic_dic["topic" + str(no + 1)] = topic

        topic_df = pd.DataFrame(topic_dic)
        topic_df.to_excel("trump3_" + str(n_topics) + ".xlsx", index=False)
        n_topics = n_topics + 10

    # model = lda
    # tf_feature_names = tf_vectorizer.get_feature_names()
    # print_top_words(lda, tf_feature_names, n_topics)
