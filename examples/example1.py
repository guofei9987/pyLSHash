from pyLSHash import LSHash
import pyLSHash

print("pyLSHash Version:", pyLSHash.__version__)

lsh = LSHash(hash_size=6, input_dim=8)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data for a
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="another vec")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])

print(res)
# %% save&load
lsh.save_uniform_planes("filename.pkl")
lsh.load_uniform_planes("filename.pkl")
