# -*- coding: utf-8 -*-
__version__ = '0.1.1'

from pyLSHash.lshash import LSHash
from .distance import hamming
from .simhash import SimHash
try:
    from fuzzy_hash import fuzzy_hash, fuzzy_compare
except:
    print("Do:\n `pip install fuzzy-hash`")