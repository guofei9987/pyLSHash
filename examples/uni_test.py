from pyLSHash import min_hash

assert min_hash.get_factors(10) == [2, 5]
assert min_hash.get_factors(16) == [2]
assert min_hash.get_factors(9) == [3]
assert min_hash.get_factors(17) == [17]

assert min_hash.get_k_coprimes(10, 3) == [1, 3, 7]
assert min_hash.get_k_coprimes(8, 10) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
