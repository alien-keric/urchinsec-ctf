import hashlib


class Hashing(object):
    def __init__(self, pt):
        self.pt = pt

    def hash_string(self):
        hash = hashlib.sha256()
        hash.update(self.pt.encode('utf-8'))
        hash_out = hash.hexdigest()

        return hash_out