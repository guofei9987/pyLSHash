import numpy as np
from pyLSHash import min_hash

n = 10  # 原向量的维度
x = np.random.randint(0, 2, n)

min_hash_val = min_hash.get_min_hash(x, n, k=4)
print(min_hash_val)
