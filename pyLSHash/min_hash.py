'''
借助定理：当 a 和 n 互素，(ax + b) % n 可生成一个全排列
b = rand()，引入随机性
时间复杂度为 O(nk)，空间复杂度为 O(k)
'''
import random


def get_factors(n: int):
    '''
    计算全部素数因子，不包括 1
    '''
    factors = list()
    i = 1
    while n > 1:
        i += 1
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n /= i
    return factors


def get_k_coprimes(n, k):
    '''
    获取前 k 个与 n 互素的数字，包括 1
    '''

    factors = get_factors(n)
    res, num = list(), 0
    while k > 0:
        num += 1
        for factor in factors:
            if num % factor == 0:
                break
        else:
            k -= 1
            res.append(num)
    return res


def get_one_min(vec, n, a) -> int:
    '''
    按照 hash(vec) = (a * vec) % n 得到 hash 值
    '''
    # random.seed(a)  # 为了每次运行结果都一致
    b = random.randint(0, n - 1)
    min_idx = n
    for i in range(n):
        if vec[i]:
            idx = (a * i + b) % n
            if idx < min_idx:
                min_idx = idx

    return min_idx


def get_min_hash(vec, n, k, seed=0):
    '''
    获取 min-hash 值
    vec：向量
    n：向量的维度
    k：min-hash 后的结果的维度
    '''
    random.seed(seed)
    return [get_one_min(vec, n, a) for a in get_k_coprimes(n, k)]
