# pyLSHash

# [pyLSHash](https://github.com/guofei9987/pyLSHash)

[![PyPI](https://img.shields.io/pypi/v/pyLSHash)](https://pypi.org/project/pyLSHash/)
[![Build Status](https://travis-ci.com/guofei9987/pyLSHash.svg?branch=master)](https://travis-ci.com/guofei9987/pyLSHash)
[![codecov](https://codecov.io/gh/guofei9987/pyLSHash/branch/master/graph/badge.svg)](https://codecov.io/gh/guofei9987/pyLSHash)
[![License](https://img.shields.io/pypi/l/pyLSHash.svg)](https://github.com/guofei9987/pyLSHash/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python->=3.5-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20|%20linux%20|%20macos-green.svg)
[![stars](https://img.shields.io/github/stars/guofei9987/pyLSHash?style=social)](https://github.com/guofei9987/pyLSHash/fork)
[![Downloads](https://pepy.tech/badge/pyLSHash)](https://pepy.tech/project/pyLSHash)


A fast Python implementation of locality sensitive hashing.

I am using [https://github.com/kayzhu/LSHash](https://github.com/kayzhu/LSHash), but it stops to update since 2013.  
So I maintain it myself.

## Highlights

- Fast hash calculation for large amount of high dimensional data through the use of `numpy` arrays.
- Built-in support for persistency through Redis.
- Multiple hash indexes support.
- Built-in support for common distance/objective functions for ranking outputs.

## Installation


`pyLSHash` depends on the following libraries:

- numpy
- redis (if persistency through Redis is needed)
- bitarray (if hamming distance is used as distance function)

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


## Main Interface


- To initialize a `LSHash` instance:


```python
LSHash(hash_size, input_dim, num_of_hashtables=1, storage=None)
```

parameters:

- ``hash_size``: The length of the resulting binary hash.
- ``input_dim``: The dimension of the input vector.
- ``num_hashtables = 1``: (optional) The number of hash tables used for multiple lookups.
- ``storage = None``: (optional) Specify the name of the storage to be used for the index storage. Options include "redis".


To index a data point of a given ``LSHash`` instance, e.g., ``lsh``:

```python
lsh.index(input_point, extra_data=None)
```

    

parameters:

- ``input_point``: The input data point is an array or tuple of numbers of input_dim.
- ``extra_data = None``: (optional) Extra data to be added along with the input_point.

To query a data point against a given ``LSHash`` instance, e.g., ``lsh``:

```python
lsh.query(query_point, num_results=None, distance_func="euclidean")
```

parameters:

- ``query_point``: The query data point is an array or tuple of numbers of input_dim.
- ``num_results = None``: (optional) The number of query results to return in ranked order. By default all results will be returned.
- ``distance_func = "euclidean"``: (optional) Distance function to use to rank the candidates. By default euclidean distance function will be used.


