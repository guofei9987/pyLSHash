# -*- coding: utf-8 -*-

import numpy as np
import pickle

from .storage import storage
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
    :param storage_config:
        (optional) A dictionary of the form `{backend_name: config}` where
        `backend_name` is the either `dict` or `redis`, and `config` is the
        configuration used by the backend. For `redis` it should be in the
        format of `{"redis": {"host": hostname, "port": port_num}}`, where
        `hostname` is normally `localhost` and `port` is normally 6379.
    """

    def __init__(self, hash_size, input_dim, num_hashtables=1, storage_config=None):

        self.hash_size = hash_size
        self.input_dim = input_dim
        self.num_hashtables = num_hashtables
        self.storage_config = storage_config or {'dict': None}

        self.uniform_planes = None
        self.hash_tables = None

        self.init_uniform_planes()
        self._init_hashtables()

    def save_uniform_planes(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.uniform_planes, f)

    def load_uniform_planes(self, filename):
        with open(filename, 'rb') as f:
            self.uniform_planes = pickle.load(f)

    def clear_storage(self):
        self.hash_tables.clear()

    def init_uniform_planes(self):
        self.uniform_planes = [np.random.randn(self.hash_size, self.input_dim)
                               for _ in range(self.num_hashtables)]

    def _init_hashtables(self):
        """ Initialize the hash tables such that each record will be in the
        form of "[storage1, storage2, ...]" """

        self.hash_tables = [storage(self.storage_config, i)
                            for i in range(self.num_hashtables)]

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

        for i, table in enumerate(self.hash_tables):
            table.append_val(key=self._hash(self.uniform_planes[i], input_point),
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

        for i, table in enumerate(self.hash_tables):
            query_hash = self._hash(self.uniform_planes[i], query_point)
            if key_hamming:
                for key in table.keys():
                    if hamming_dist(key, query_hash) < 2:
                        candidates.update(table.get_list(key))
            else:
                candidates.update(table.get_list(query_hash))

        # rank candidates by distance function
        candidates = [(ix, dist_func(query_point, ix[0]))
                      for ix in candidates]
        candidates.sort(key=lambda x: x[1])

        return candidates[:num_results] if num_results else candidates


def hamming_dist(key1, key2):
    return bin(int(key1, base=2) ^ int(key2, base=2))[2:].count('1')
