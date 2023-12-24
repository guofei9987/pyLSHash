from pyLSHash import LSHash
import pyLSHash

print("pyLSHash Version:", pyLSHash.__version__)

lsh = LSHash(hash_size=6, input_dim=8)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

# test hamming_dist
res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])

print(res)

assert res[0][0][0] == (1, 2, 3, 4, 5, 6, 7, 8)

res2 = lsh.query([1, 2, 3, 4, 5, 6, 7, 7], key_hamming=True)
assert res2[0][0][0] == (1, 2, 3, 4, 5, 6, 7, 8)


# %% user defined distance function

def l1norm_dist(x, y):
    return sum(abs(x - y))


res2 = lsh.query([1, 2, 3, 4, 5, 6, 7, 7], dist_func=l1norm_dist)

print(res2)
