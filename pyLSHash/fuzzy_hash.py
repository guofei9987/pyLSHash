try:
    from fuzzy_hash import fuzzy_hash, fuzzy_compare
except:
    fuzzy_hash = fuzzy_compare = None


class FuzzyHash:
    def __int__(self):
        if fuzzy_hash is None:
            raise ImportError("fuzzy-hash not installed\n see: https://github.com/guofei9987/fuzzy-hash")

    def get_hash(self, str1: bytes) -> bytes:
        return fuzzy_hash(str1)

    def compare(self, hash1: bytes, hash2: bytes) -> int:
        return fuzzy_compare(hash1, hash2)
