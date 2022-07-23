from pyLSHash import LSHash
from pyLSHash.storage import StorageBase
import redis
import json


class MyStorage(StorageBase):
    def __init__(self):
        self.storage = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def keys(self, pattern="*"):
        return self.storage.keys(pattern)

    def set_val(self, key, val):
        self.storage.set(key, val)

    def get_val(self, key):
        return self.storage.get(key)

    def append_val(self, key, val):
        self.storage.rpush(key, json.dumps(val))

    def get_list(self, key):
        res_list = [json.loads(val) for val in self.storage.lrange(key, 0, -1)]
        return tuple((tuple(item[0]), item[1]) for item in res_list)

    def clear(self):
        for key in self.storage.keys():
            self.storage.delete(key)


lsh = LSHash(hash_size=6, input_dim=8
             , storage_instance=MyStorage())

lsh.index([1, 2, 3, 4, 5, 6, 7, 8])
lsh.index([2, 3, 4, 5, 6, 7, 8, 9])
# attach extra_data
lsh.index([2, 3, 4, 5, 6, 7, 8, 9], extra_data="some vector info")
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])
lsh.index([10, 12, 99, 1, 5, 31, 2, 3])

res = lsh.query([1, 2, 3, 4, 5, 6, 7, 7])
print(res)
