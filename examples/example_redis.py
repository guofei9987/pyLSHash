from pyLSHash import LSHash
from pyLSHash.storage import RedisStorage
import pyLSHash

print("pyLSHash Version:", pyLSHash.__version__)
print("run this firstly > redis-server ")

lsh = LSHash(hash_size=6, input_dim=8
             , storage_instance=RedisStorage({'host': 'localhost', 'port': 6379, 'decode_responses': True}))

lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
print(res)
