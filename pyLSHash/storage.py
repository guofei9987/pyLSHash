# -*- coding: utf-8 -*-

import json
from abc import ABCMeta, abstractmethod


class StorageBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, config):
        """ An abstract class used as an adapter for storages. """
        pass

    @abstractmethod
    def keys(self):
        """ Returns a list of binary hashes that are used as dict keys. """
        pass

    @abstractmethod
    def set_val(self, key, val):
        """ Set `val` at `key`, note that the `val` must be a string. """
        pass

    @abstractmethod
    def get_val(self, key):
        """ Return `val` at `key`, note that the `val` must be a string. """
        pass

    @abstractmethod
    def append_val(self, key, val):
        """ Append `val` to the list stored at `key`.

        If the key is not yet present in storage, create a list with `val` at
        `key`.
        """
        pass

    @abstractmethod
    def get_list(self, key):
        """ Returns a list stored in storage at `key`.

        This method should return a list of values stored at `key`. `[]` should
        be returned if the list is empty or if `key` is not present in storage.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """ Clear all data
        """
        pass


class InMemoryStorage(StorageBase):
    def __init__(self, config):
        self.name = 'dict'
        self.storage = dict()

    def keys(self):
        return self.storage.keys()

    def set_val(self, key, val):
        self.storage[key] = val

    def get_val(self, key):
        return self.storage[key]

    def append_val(self, key, val):
        self.storage.setdefault(key, []).append(val)

    def get_list(self, key):
        return self.storage.get(key, [])

    def clear(self):
        self.storage = dict()


class RedisStorage(StorageBase):
    def __init__(self, config):
        try:
            import redis
        except ImportError:
            raise ImportError("redis-py is required to use Redis as storage.")

        self.name = 'redis'
        self.storage = redis.StrictRedis(**config)

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
