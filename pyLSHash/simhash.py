"""
simhash
int: return the origin int
dict: do hash for every item, and get the weighted average.
str: get lower -> get valid chars with regex -> get rolling slice(window=4), transform to dict, and get hash as dict
Iterable: transform to dict, and get hash as dict
"""

import collections
import hashlib
import re
from collections import Counter
from collections.abc import Iterable

import numpy as np


def int_to_bytes(n, length):
    return n.to_bytes(length, 'big')


def bytes_to_int(b):
    return int.from_bytes(b, 'big')


def _hashfunc(x):
    return hashlib.md5(x).digest()


class SimHash(object):
    def __init__(self, len_hash=64):
        self.val = None
        self.regex = re.compile(r'[\w\u4e00-\u9fcc]+')
        self.hash_func = _hashfunc

        # f： dimensions of fingerprints, in bits
        assert len_hash % 8 == 0, 'len_hash must be a multiple of 8'

        self.len_hash = len_hash
        self.f_bytes = len_hash // 8

    def get_hash(self, val):
        if isinstance(val, int):
            # TODO:过大的数不行
            return val
        elif isinstance(val, dict):
            return self.get_hash_dict(val)
        elif isinstance(val, str):
            return self.get_hash_str(val)
        elif isinstance(val, Iterable):
            return self.get_hash_iterator(val)

        Exception('Bad parameter with type {}'.format(type(val)))

    def get_hash_str(self, content: str):
        # 去除无关的字符
        content = ''.join(self.regex.findall(content.lower()))
        width = 4  # token 的长度
        # 每个 offset 都要取出来
        content_token_lst = [content[i:i + width] for i in range(max(len(content) - width + 1, 1))]
        features = Counter(content_token_lst)
        return self.get_hash_dict(features)

    def get_hash_dict(self, features: dict):
        hash_func = self.hash_func
        truncate_mask = (1 << self.len_hash) - 1

        batch = list()
        cnt = 0
        for feature, weight in features.items():
            # 截断，只要末尾。md5的结果长度 16，这里取 f_bytes，长度为 8
            h = hash_func(feature.encode('utf-8'))[-self.f_bytes:]
            #     TODO：
            # 默认的_hashfunc（hashlib.md5(x).digest() ）返回 byte 类型
            # 自定义的有时候返回 int
            batch.append(self._bitarray_from_bytes(h) * weight)
            #     TODO:需要注意这里内存过大的可能性
            cnt += weight

        sums = np.sum(batch, 0)
        val = bytes_to_int(np.packbits(sums > cnt / 2).tobytes())
        return val

    def get_hash_iterator(self, val):
        return self.get_hash_dict(collections.Counter(val))

    def _sum_hashes(self, digests):
        # 转二进制
        bitarray = self._bitarray_from_bytes(b''.join(digests))
        rows = np.reshape(bitarray, (-1, self.len_hash))
        return np.sum(rows, 0)

    @staticmethod
    def _bitarray_from_bytes(b):
        return np.unpackbits(np.frombuffer(b, dtype='>B'))
