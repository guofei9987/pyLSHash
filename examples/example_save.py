from pyLSHash import LSHash
import pyLSHash

print("pyLSHash Version:", pyLSHash.__version__)

lsh = LSHash(hash_size=6, input_dim=8)
# %% save&load
lsh.save_uniform_planes("filename.pkl")
lsh.load_uniform_planes("filename.pkl")

# %% clear all indexed data
lsh.clear_storage()
