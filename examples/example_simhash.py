import jieba
import collections
from pyLSHash import SimHash
from pyLSHash import hamming
from collections import defaultdict

sentence = '''
近期，有一部热播硬核电视剧引发全网关注。与其他硬核电视剧不同的是，这部电视剧真的硬“核”，含“核”量高达100%。
这就是《许你万家灯火》——首部全景反映我国核电工业发展历程的电视剧。
《许你万家灯火》极具年代感，这是因为取景地之一是中国核动力的发源地——九〇九基地。
中国第一代核潜艇研发实验基地
也是中国核动力研究设计院的前身

剧组在基地里面内置景，1:1复刻了主要场景十余个，
包括第一座陆上模式堆主控室、核电大院、核电办公楼、核电家属楼、零号点、医院、图书馆、大礼堂等，
高度还原了老一辈核工业人的研发和生活环境。

而《许你万家灯火》的创作题材，便是中国完全自主知识产权的三代核电技术——“华龙一号”。
从核潜艇研发起步的中国核工业
如何实现拥有世界一流核电站的梦想？
'''

sim_hash = SimHash()

# %% replace + input string

sim_hash_val1 = sim_hash.get_hash(sentence)

words_to_modify = ['纪录片', '电影', '视频']
for word in words_to_modify:
    sentence2 = sentence.replace('电视剧', word)
    sim_hash_val2 = sim_hash.get_hash(sentence2)
    corr = 1 - hamming(sim_hash_val1, sim_hash_val2) / sim_hash.len_hash
    assert corr > 0.85

# %% insert + input string
for insert_idx in range(0, len(sentence)):
    sentence2 = sentence[:insert_idx] + "随机插入" + sentence[insert_idx:]
    sim_hash_val2 = sim_hash.get_hash(sentence2)
    corr = 1 - hamming(sim_hash_val1, sim_hash_val2) / sim_hash.len_hash
    assert corr > 0.85

# %% delete + input string

for insert_idx in range(0, len(sentence) - 5):
    sentence2 = sentence[:insert_idx] + sentence[insert_idx + 5:]
    sim_hash_val2 = sim_hash.get_hash(sentence2)
    hamming_distance = hamming(sim_hash_val1, sim_hash_val2)
    corr = 1 - hamming(sim_hash_val1, sim_hash_val2) / sim_hash.len_hash
    assert corr > 0.85

# %% replace + input features
sim_hash_val1 = sim_hash.get_hash(collections.Counter(jieba.cut(sentence)))

words_to_modify = ['纪录片', '电影', '视频']
for word in words_to_modify:
    sentence2 = sentence.replace('电视剧', word)
    sim_hash_val2 = sim_hash.get_hash(collections.Counter(jieba.cut(sentence2)))
    corr = 1 - hamming(sim_hash_val1, sim_hash_val2) / sim_hash.len_hash
    assert corr > 0.90

# %% insert + input features
for insert_idx in range(0, len(sentence)):
    sentence2 = sentence[:insert_idx] + "随机插入" + sentence[insert_idx:]
    sim_hash_val2 = sim_hash.get_hash(collections.Counter(jieba.cut(sentence2)))
    corr = 1 - hamming(sim_hash_val1, sim_hash_val2) / sim_hash.len_hash
    assert corr > 0.9

# %% delete + input features
for insert_idx in range(0, len(sentence) - 5):
    sentence2 = sentence[:insert_idx] + sentence[insert_idx + 5:]
    sim_hash_val2 = sim_hash.get_hash(collections.Counter(jieba.cut(sentence2)))
    corr = 1 - hamming(sim_hash_val1, sim_hash_val2) / sim_hash.len_hash
    assert corr > 0.9
