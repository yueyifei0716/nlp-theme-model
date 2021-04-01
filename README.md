# Keyword automatic detection algorithms

With the rapid development of Weibo, Twitter and other social media, self media and new media,
detecting keywords from large amounts of text data updated in read time has become a critical problem.

The keyword detection problem aims at predicting important information that has not been
discovered before the keywords are frequently searched by users. However, compared with the traditional
media data, the media data in the new era has 3 features:

* Strong timeliness
* More personalized and colloquial language
* Relatively short length

We have implemented some baselines which can be used for keywords detection
including TF-IDF, LDA, Word2vec, and proposed our new method based on these basic methods
which currently combining TF-IDF and LDA.

## Table of Contents

* [Models and Implementations](#models-and-implementations)
  * [Preprocess](#preprocess)
  * [Baselines](#baselines)
    * [TF-IDF](#tf-idf)
    * [LDA](#lda)
    * [Word2vec](#word2vec)
  * [New method](#new-method)

## Models and Implementations

### Preprocess

### Baselines

#### TF-IDF

| Model | Reference (Paper) |

[comment]: <> (|-------|-------------------|)

[comment]: <> (| [MNIST]&#40;vision/image_classification&#41; | A basic model to classify digits from the [MNIST dataset]&#40;http://yann.lecun.com/exdb/mnist/&#41; |)

[comment]: <> (| [ResNet]&#40;vision/image_classification&#41; | [Deep Residual Learning for Image Recognition]&#40;https://arxiv.org/abs/1512.03385&#41; |)

[comment]: <> (| [EfficientNet]&#40;vision/image_classification&#41; | [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks]&#40;https://arxiv.org/abs/1905.11946&#41; |)

#### LDA

| Model | Reference (Paper) |

[comment]: <> (|-------|-------------------|)

[comment]: <> (| [RetinaNet]&#40;vision/detection&#41; | [Focal Loss for Dense Object Detection]&#40;https://arxiv.org/abs/1708.02002&#41; |)

[comment]: <> (| [Mask R-CNN]&#40;vision/detection&#41; | [Mask R-CNN]&#40;https://arxiv.org/abs/1703.06870&#41; |)

[comment]: <> (| [ShapeMask]&#40;vision/detection&#41; | [ShapeMask: Learning to Segment Novel Objects by Refining Shape Priors]&#40;https://arxiv.org/abs/1904.03239&#41; |)

[comment]: <> (| [SpineNet]&#40;vision/detection&#41; | [SpineNet: Learning Scale-Permuted Backbone for Recognition and Localization]&#40;https://arxiv.org/abs/1912.05027&#41; |)

#### Word2vec

| Model | Reference (Paper) |

[comment]: <> (|-------|-------------------|)

[comment]: <> (| [RetinaNet]&#40;vision/detection&#41; | [Focal Loss for Dense Object Detection]&#40;https://arxiv.org/abs/1708.02002&#41; |)

[comment]: <> (| [Mask R-CNN]&#40;vision/detection&#41; | [Mask R-CNN]&#40;https://arxiv.org/abs/1703.06870&#41; |)

[comment]: <> (| [ShapeMask]&#40;vision/detection&#41; | [ShapeMask: Learning to Segment Novel Objects by Refining Shape Priors]&#40;https://arxiv.org/abs/1904.03239&#41; |)

[comment]: <> (| [SpineNet]&#40;vision/detection&#41; | [SpineNet: Learning Scale-Permuted Backbone for Recognition and Localization]&#40;https://arxiv.org/abs/1912.05027&#41; |)

### New method

| Model | |

[comment]: <> (|-------|-------------------|)

[comment]: <> (| [ALBERT &#40;A Lite BERT&#41;]&#40;nlp/albert&#41; | [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations]&#40;https://arxiv.org/abs/1909.11942&#41; |)

[comment]: <> (| [BERT &#40;Bidirectional Encoder Representations from Transformers&#41;]&#40;nlp/bert&#41; | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding]&#40;https://arxiv.org/abs/1810.04805&#41; |)

[comment]: <> (| [NHNet &#40;News Headline generation model&#41;]&#40;nlp/nhnet&#41; | [Generating Representative Headlines for News Stories]&#40;https://arxiv.org/abs/2001.09386&#41; |)

[comment]: <> (| [Transformer]&#40;nlp/transformer&#41; | [Attention Is All You Need]&#40;https://arxiv.org/abs/1706.03762&#41; |)

[comment]: <> (| [XLNet]&#40;nlp/xlnet&#41; | [XLNet: Generalized Autoregressive Pretraining for Language Understanding]&#40;https://arxiv.org/abs/1906.08237&#41; |)

[comment]: <> (## Citing TF Official Model Garden)

[comment]: <> (To cite this repository:)

[comment]: <> (```)

[comment]: <> (@software{tfmodels2020github,)

[comment]: <> (  author = {Chen Chen and Xianzhi Du and Le Hou and Jaeyoun Kim and Pengchong)

[comment]: <> (  Jin and Jing Li and Yeqing Li and Abdullah Rashwan and Hongkun Yu},)

[comment]: <> (  title = {TensorFlow Official Model Garden},)

[comment]: <> (  url = {https://github.com/tensorflow/models/tree/master/official},)

[comment]: <> (  year = {2020},)

[comment]: <> (})

[comment]: <> (```)
