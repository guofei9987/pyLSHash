from pyLSHash import LSHash

lsh = LSHash(hash_size=6, input_dim=8)
lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.query([1, 2, 3, 4, 5, 6, 7, 7])

# %%
lsh.save_uniform_planes("filename.pkl")
lsh.load_uniform_planes("filename.pkl")
