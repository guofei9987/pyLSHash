def hamming(hash_val1: int, hash_val2: int) -> int:
    '''
    hamming distance
    '''
    dist, xor = 0, hash_val1 ^ hash_val2
    while xor:
        dist += 1
        xor &= xor - 1
    return dist
