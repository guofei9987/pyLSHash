# -*- coding: utf-8 -*-

import numpy as np
import pickle

from . import storage
from . import dist_func


class LSHash(object):
    """ LSHash implments locality sensitive hashing using random projection for
    input vectors of dimension `input_dim`.

    Attributes:

    :param hash_size:
        The length of the resulting binary hash in integer. E.g., 32 means the
        resulting binary hash will be 32-bit long.
    :param input_dim:
        The dimension of the input vector. E.g., a grey-scale picture of 30x30
        pixels will have an input dimension of 900.
    :param num_hashtables:
        (optional) The number of hash tables used for multiple lookups.
    :param storage:
        An object to store data
    """

    def __init__(self, hash_size, input_dim, num_hashtables=1,
                 storage_instance: storage.StorageBase = storage.InMemoryStorage('')):

        self.hash_size = hash_size
        self.input_dim = input_dim
        self.num_hashtables = num_hashtables
        self.storage_instance = storage_instance

        self.uniform_planes = None

        self.init_uniform_planes()

    def save_uniform_planes(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.uniform_planes, f)

    def load_uniform_planes(self, filename):
        with open(filename, 'rb') as f:
            self.uniform_planes = pickle.load(f)

    def clear_storage(self):
        self.storage_instance.clear()

    def init_uniform_planes(self):
        self.uniform_planes = [np.random.randn(self.hash_size, self.input_dim)
                               for _ in range(self.num_hashtables)]

    def _hash(self, planes, input_point):
        """ Generates the binary hash for `input_point` and returns it.

        :param planes:
            The planes are random uniform planes with a dimension of
            `hash_size` * `input_dim`.
        :param input_point:
            A Python tuple or list object that contains only numbers.
            The dimension needs to be 1 * `input_dim`.
        """

        projections = np.dot(planes, np.array(input_point))
        return "".join(['1' if i > 0 else '0' for i in projections])

    def index(self, input_point, extra_data=''):
        """ Index a single input point by adding it to the selected storage.

        If `extra_data` is provided, it will become the value of the dictionary
        {input_point: extra_data}, which in turn will become the value of the
        hash table. `extra_data` needs to be JSON serializable if in-memory
        dict is not used as storage.

        :param input_point:
            A list, or tuple, or numpy ndarray object that contains numbers
            only. The dimension needs to be 1 * `input_dim`.
            This object will be converted to Python tuple and stored in the
            selected storage.
        :param extra_data:
            (optional) Needs to be a JSON-serializable object: list, dicts and
            basic types such as strings and integers.
        """

        if isinstance(input_point, np.ndarray):
            input_point = input_point.tolist()

        value = (tuple(input_point), extra_data)

        for i in range(self.num_hashtables):
            self.storage_instance.append_val(
                key=str(i) + "|" + self._hash(self.uniform_planes[i], input_point),
                val=value)

    def query(self, query_point, num_results=None
              , dist_func=dist_func.euclidean_dist_square
              , key_hamming=False):
        """ Takes `query_point` which is either a tuple or a list of numbers,
        returns `num_results` of results as a list of tuples that are ranked
        based on the supplied metric function `distance_func`.

        :param query_point:
            A list, or tuple, or numpy ndarray that only contains numbers.
            The dimension needs to be 1 * `input_dim`.
            Used by :meth:`._hash`.
        :param num_results:
            (optional) Integer, specifies the max amount of results to be
            returned. If not specified all candidates will be returned as a
            list in ranked order.
        """

        candidates = set()
        query_point = np.array(query_point)

        if key_hamming:
            for i in range(self.num_hashtables):
                query_hash = self._hash(self.uniform_planes[i], query_point)
                for key in self.storage_instance.keys():
                    key1, key2 = key.split('|')
                    if key1 == str(i):
                        if hamming_dist(key2, query_hash) < 2:
                            candidates.update(self.storage_instance.get_list(key2))

        if not key_hamming:
            for i in range(self.num_hashtables):
                query_hash = self._hash(self.uniform_planes[i], query_point)
                candidates.update(self.storage_instance.get_list(str(i) + '|' + query_hash))


        # rank candidates by distance function
        candidates = [(ix, dist_func(query_point, np.array(ix[0])))
                      for ix in candidates]
        candidates.sort(key=lambda x: x[1])

        return candidates[:num_results] if num_results else candidates


def hamming_dist(key1, key2):
    return bin(int(key1, base=2) ^ int(key2, base=2))[2:].count('1')
