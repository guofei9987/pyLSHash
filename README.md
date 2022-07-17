# [pyLSHash](https://github.com/guofei9987/pyLSHash)

[![PyPI](https://img.shields.io/pypi/v/pyLSHash)](https://pypi.org/project/pyLSHash/)
[![Build Status](https://app.travis-ci.com/guofei9987/pyLSHash.svg?branch=main)](https://app.travis-ci.com/guofei9987/pyLSHash)
[![codecov](https://codecov.io/gh/guofei9987/pyLSHash/branch/main/graph/badge.svg)](https://codecov.io/gh/guofei9987/pyLSHash)
[![License](https://img.shields.io/pypi/l/pyLSHash.svg)](https://github.com/guofei9987/pyLSHash/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/pyLSHash?style=social)](https://github.com/guofei9987/pyLSHash/fork)


A fast Python implementation of locality sensitive hashing.

I am using [https://github.com/kayzhu/LSHash](https://github.com/kayzhu/LSHash), but it stops to update since 2013.  
So I maintain it myself, and I have made a lot of improvement based on it.

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

To create 6-bit hashes for input data of 8 dimensions:


```python
from pyLSHash import LSHash

lsh = LSHash(6, 8)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
```

>[((1, 2, 3, 4, 5, 6, 7, 8), 1.0),
((2, 3, 4, 5, 6, 7, 8, 9), 11)]

## Use Redis

```python
from pyLSHash import LSHash
import pyLSHash

storage_config = {"redis": {
    'host': 'localhost', 'port': 6379, 'decode_responses': True}
}

lsh = LSHash(hash_size=6, input_dim=8, storage_config=storage_config)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
print(res)
```

## save&load model

```python
lsh.save_uniform_planes("filename.pkl")
lsh.load_uniform_planes("filename.pkl")
```

clear indexed data
```python
lsh.clear_storage()
```