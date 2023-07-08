from pyLSHash import min_hash

k = 3  # minHash 值的维度

x1 = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
x2 = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0]

n = len(x1)  # 向量的维度
min_hash_val1 = min_hash.get_min_hash(x1, n, k)
min_hash_val2 = min_hash.get_min_hash(x2, n, k)
print(min_hash_val1)
print(min_hash_val2)
assert min_hash_val1 == min_hash_val2
