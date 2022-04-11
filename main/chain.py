import hashlib
from numpy import block
from main.block import Block

class Chain():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        self.data_pool = []
        self.genesis_block()

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2**(256-self.difficulty) and block.prev_hash == self.blocks[-1].hash

    def append_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def append_to_pool(self, data):
        self.data_pool.append(data)
    
    def genesis_block(self):
        h = hashlib.sha256()
        h.update("".encode('utf-8'))
        origin = Block("Origin", h)
        origin.mine(self.difficulty)
        self.blocks.append(origin)

    def mine(self):
        if len(self.data_pool) > 0:
            data = self.data_pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.difficulty)
            self.append_to_chain(block)
            '''print("\n\n**************")
            print("Hash: ", block.hash.hexdigest())
            print("Previous Hash:\t\t", block.prev_hash.hexdigest())
            print("Nonce:\t\t", block.num)
            print("Data:\t\t", block.data)
            print("\n\n**************")'''
