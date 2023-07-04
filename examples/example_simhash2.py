from pyLSHash import SimHash
from pyLSHash import hamming

simhash = SimHash()

# %%
h0 = simhash.get_hash('How are you? I AM fine. Thanks. And you?')
h1 = simhash.get_hash('How are you? I AM fine. Thanks. And you?')
h2 = simhash.get_hash('How old are you ? :-) i am fine. Thanks. And you?')

assert hamming(h0, h1) == 0
assert hamming(h0, h2) != 0

# %%
sh1 = simhash.get_hash('你好　世界！　　呼噜。')
sh2 = simhash.get_hash('你好，世界　呼噜')
assert hamming(sh1, sh2) == 0

# %%


sh4 = simhash.get_hash('How are you? I Am fine. ablar ablar xyz blar blar blar blar blar blar blar Thanks.')
sh5 = simhash.get_hash('How are you i am fine.ablar ablar xyz blar blar blar blar blar blar blar than')
sh6 = simhash.get_hash('How are you i am fine.ablar ablar xyz blar blar blar blar blar blar blar thank')

assert hamming(sh4, sh5) < 3
assert hamming(sh5, sh6) < 3

# %%
shs = [simhash.get_hash(s) for s in ('aa', 'aaa', 'aaaa', 'aaaab', 'aaaaabb', 'aaaaabbb')]

for i, sh1 in enumerate(shs):
    for j, sh2 in enumerate(shs):
        if i != j:
            assert sh1 != sh2

# %%
assert simhash.get_hash(0) == 0
assert simhash.get_hash(9223372036854775808) == 9223372036854775808

# %%
from sklearn.feature_extraction.text import TfidfVectorizer

data = [
    'How are you? I Am fine. blar blar blar blar blar Thanks.',
    'How are you i am fine. blar blar blar blar blar than',
    'This is simhash test.',
    'How are you i am fine. blar blar blar blar blar thank1'
]

tf_idf_vect = TfidfVectorizer()
tf_idf = tf_idf_vect.fit_transform(data)
vocabulary = dict((i, w) for w, i in tf_idf_vect.vocabulary_.items())

shs = []
for i in range(len(data)):
    Di = tf_idf.getrow(i)
    # features as dict of {token: weight}
    features = dict(zip([vocabulary[j] for j in Di.indices], Di.data))
    shs.append(simhash.get_hash(features))

assert hamming(shs[0], shs[2]) > hamming(shs[0], shs[1]) > 0

# %% user defined hash functions
import hashlib


def my_hash_func1(x) -> bytes:
    return hashlib.md5(x).digest()


def my_hash_func2(x) -> bytes:
    return hashlib.sha256(x).digest()


simhash.hash_func = my_hash_func1
sh1 = simhash.get_hash("hello")
simhash.hash_func = my_hash_func2
sh2 = simhash.get_hash("hello")

assert sh1 != sh2
