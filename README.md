# [pyLSHash](https://github.com/guofei9987/pyLSHash)

[![PyPI](https://img.shields.io/pypi/v/pyLSHash)](https://pypi.org/project/pyLSHash/)
[![Python package](https://github.com/guofei9987/pyLSHash/actions/workflows/python-package.yml/badge.svg)](https://github.com/guofei9987/pyLSHash/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/guofei9987/pyLSHash/branch/main/graph/badge.svg)](https://codecov.io/gh/guofei9987/pyLSHash)
[![License](https://img.shields.io/pypi/l/pyLSHash.svg)](https://github.com/guofei9987/pyLSHash/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/pyLSHash?style=social)](https://github.com/guofei9987/pyLSHash/fork)


A fast Python implementation of locality sensitive hashing.



| Algorithm | Function                                                                                                                                           | Application                         | Features                                                                              |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------|
| fuzzy-hash| Map text or string or file to 64-bits (or other) hash values. Similar contents hash similar hash values                                            | Fast compare similar contents       | Suitable for text/string/file                     
| min-hash  | Map sets to signature matrices and find similar sets by calculating Jaccard similarity                                                             | Similarity retrieval                | Suitable for text, network, audio, and other data                                     |
| SimHash   | Convert high-dimensional data such as text and images into fixed-length vectors, and map similar vectors to the same bucket through hash functions | Text and image similarity retrieval | Suitable for high-dimensional data                                                    |
| aHash     | Compress images to a fixed size and map similar images to the same bucket through hash functions                                                   | Similar image retrieval             | Has some robustness to scaling and slight deformations                                |
| dHash     | Convert images to grayscale and calculate difference values, then map similar images to the same bucket through hash functions                     | Similar image retrieval             | Has some robustness to scaling and slight deformations                                |
| pHash     | Convert images to DCT coefficients and map similar images to the same bucket through hash functions                                                | Similar image retrieval             | Has some robustness to scaling, brightness, translation, rotation, and noise addition |
| LSH       | Map high-dimensional vectors to low-dimensional space and map similar vectors to the same bucket through hash functions                            | Fast search for approximate vectors | Suitable for large-scale high-dimensional data                                        |





## Highlights

- Fast hash calculation for large amount of high dimensional data through the use of `numpy` arrays.
- Built-in support for persistency through Redis.
- Multiple hash indexes support.
- Built-in support for common distance/objective functions for ranking outputs.

## Installation


`pyLSHash` depends on the following libraries:

- numpy
- redis (if persistency through Redis is needed)


To install:


```bash
$ pip install pyLSHash
```

## Quickstart

### fuzzy-hash

```python
sentence1 = '''
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

sentence2 = '''
你好：
近期，有一部热播硬核节目引发全网关注。与其他硬核节目不同的是，这部电视剧真的硬“核”，含“核”量高达100%。
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
感谢！
'''

from pyLSHash import FuzzyHash

fuzzy_hash = FuzzyHash()

hash1 = fuzzy_hash.get_hash(sentence1.encode('utf-8'))
hash2 = fuzzy_hash.get_hash(sentence2.encode('utf-8'))

print(hash1)
print(hash2)

corr = fuzzy_hash.compare(hash1, hash2)
print('corr = {}%'.format(corr))
```
>b'24:NCRqxthHLDYTvxiiIhNM+Nkr6gy8C4xB6YR514cLCxd6tXKlru2uEj:tBHATdN+OuNOZrIxnAa'
b'24:TsoR7RmxthHLDYTvxiiIhNM+Nkr6gy8o4xB6YR514cLCxd6tXilru2uEUv:fR7RmBHATdN+OulOZrIxdA7'
corr = 86%

Look at [examples/example_fuzzy_hash.py](examples/example_fuzzy_hash.py)


### SimHash

```py
from pyLSHash import SimHash, hamming

sim_hash = SimHash()

sh1 = sim_hash.get_hash(sentence1)
sh2 = sim_hash.get_hash(sentence2)

corr = 1 - hamming(sh1, sh2) / sim_hash.len_hash
print(sh1)
print(sh2)
print('corr = {}'.format(corr))
```

>957004571726091744  
943493772323861728  
corr = 0.890625  


Look at [examples/example_simhash.py](examples/example_simhash.py)

### minHash


```python
from pyLSHash import min_hash

k = 3  # minHash 值的维度

x1 = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
x2 = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0]

n = len(x1)  # 向量的维度
min_hash_val1 = min_hash.get_min_hash(x1, n, k)
min_hash_val2 = min_hash.get_min_hash(x2, n, k)
print(min_hash_val1)
print(min_hash_val2)
```

>[1, 0, 0]  
[1, 0, 0]  


Look at [examples/example_min_hash.py](examples/example_min_hash.py)


### aHash/dHash/pHash

aHash
```python
a_hash_img1 = img_hash.a_hash(PIL.Image.open(img1))
a_hash_img2 = img_hash.a_hash(PIL.Image.open(img2))
hamming_distance = hamming(a_hash_img1, a_hash_img2)
```


dHash
```python
d_hash_img1 = img_hash.d_hash(PIL.Image.open(img1))
d_hash_img2 = img_hash.d_hash(PIL.Image.open(img2))
hamming_distance = hamming(d_hash_img1, d_hash_img2)
```


pHash
```python
p_hash_img1 = img_hash.p_hash(PIL.Image.open(img1))
p_hash_img2 = img_hash.p_hash(PIL.Image.open(img2))
hamming_distance = hamming(p_hash_img1, p_hash_img2)
```

outputs:
>[aHash]: img1 = 0xffc3c3db819f0000, img2 = 0xffc3c3cb819f0000  
hamming_distance = 1  
[dHash]: img1 = 0x7ffae0c63d188743, img2 = 0x7ffae0c23d188743  
hamming_distance = 1  
[pHash]: img1 = 0xa8a0008200000000, img2 = 0xa8a0008200000000  
hamming_distance = 0  



Look at [examples/example_img_hash.py](examples/example_img_hash.py)



## LSHash
To create 6-bit hashes for input data of 8 dimensions:


```python
from pyLSHash import LSHash

lsh = LSHash(hash_size=6, input_dim=8)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
```

>[((1, 2, 3, 4, 5, 6, 7, 8), 1.0),
((2, 3, 4, 5, 6, 7, 8, 9), 11)]

### User defined distance function

```python
def l1norm_dist(x, y):
    return sum(abs(x - y))


res2 = lsh.query([1, 2, 3, 4, 5, 6, 7, 7], dist_func=l1norm_dist)

print(res2)
```


### Use Redis

```python
from pyLSHash import LSHash

lsh = LSHash(hash_size=6, input_dim=8
             , storage_instance=RedisStorage({'host': 'localhost', 'port': 6379, 'decode_responses': True}))

lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
```

### Use other database as storage

```python
from pyLSHash import LSHash
from pyLSHash.storage import StorageBase
import redis
import json


class MyStorage(StorageBase):
    def __init__(self):
        self.storage = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def keys(self, pattern="*"):
        return self.storage.keys(pattern)

    def set_val(self, key, val):
        self.storage.set(key, val)

    def get_val(self, key):
        return self.storage.get(key)

    def append_val(self, key, val):
        self.storage.rpush(key, json.dumps(val))

    def get_list(self, key):
        res_list = [json.loads(val) for val in self.storage.lrange(key, 0, -1)]
        return tuple((tuple(item[0]), item[1]) for item in res_list)

    def clear(self):
        for key in self.storage.keys():
            self.storage.delete(key)


lsh = LSHash(hash_size=6, input_dim=8
             , storage_instance=MyStorage())

lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
```


### save&load model

```python
lsh.save_uniform_planes("filename.pkl")
lsh.load_uniform_planes("filename.pkl")
```

clear indexed data
```python
lsh.clear_storage()
```

## Other examples

- Examples for min-hash ：[examples/example_min_hash.py](examples/example_min_hash.py)
- Examples for SimHash ：[examples/example_simhash.py](examples/example_simhash.py), [examples/example_simhash2.py](examples/example_simhash2.py)
- Examples for aHash ：[examples/example_img_hash.py](examples/example_img_hash.py)
- Examples for dHash ： [examples/example_img_hash.py](examples/example_img_hash.py)
- Examples for pHash ：[examples/example_img_hash.py](examples/example_img_hash.py)