import hashlib

class Block():
    def __init__(self, data, previous_hash):
        self.data = data
        self.prev_hash = previous_hash
        self.hash = hashlib.sha256()
        self.num = 0
    
    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            self.num += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def __str__(self):
        return "{}{}{}".format(self.prev_hash.hexdigest(), self.data, self.num)