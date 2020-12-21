# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import word2vec

# 文件位置需要改为自己的存放路径
# 将文本分词

sentences = word2vec.LineSentence('/Users/yueyifei/Code/python_test/NLP/theme_model/trump2.txt')
# 训练语料
path = get_tmpfile("word2vec.model")  # 创建临时文件
model = word2vec.Word2Vec(sentences)
# model.save("word2vec.model")
# model = Word2Vec.load("word2vec.model")
# 输入与“贪污”相近的100个词
# for key in model.wv.similar_by_word('贪污', top n = 100):
#     print(key)

w2c = dict()
for item in model.wv.vocab:
    w2c[item] = model.wv.vocab[item].count
w2cSorted = dict(sorted(w2c.items(), key=lambda x: x[1], reverse=True))
w2cSortedList = list(w2cSorted.keys())
result = model.wv.index2entity[:20]
print(result)
