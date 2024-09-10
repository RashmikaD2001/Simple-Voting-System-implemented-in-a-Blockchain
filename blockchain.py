import time
import hashlib

def hashgenerator(data, difficulty):
    nonceval = 0
    result = hashlib.sha256(data.encode()).hexdigest()

    while result[:difficulty] != '0' * difficulty:
        nonceval += 1
        result = hashlib.sha256((data + str(nonceval)).encode()).hexdigest()

    return [nonceval, result]  # Return both nonce and hash

def hashfunc(data):
    return hashlib.sha256(data.encode()).hexdigest() #Return hash value to varify the hash value of block


class Block:
    def __init__(self, vote, index, hashval, timestamp, previous_hash, nonce):
        self.vote = vote
        self.index = index
        self.hashval = hashval  # The current block's hash
        self.previous_hash = previous_hash  # The previous block's hash
        self.timestamp = timestamp  # Timestamp of block creation
        self.nonce = nonce  # The proof of work value


class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty

        # Creating the Genesis Block (the first block in the chain)
        hashLast = hashgenerator('last_gen', self.difficulty)
        genesis = Block('gen_data', 0, hashLast[1], time.time(), '0', hashLast[0])
        self.chain = [genesis]  # Initialize the blockchain with the genesis block

    def addblock(self, data):
        previous_hash = self.chain[-1].hashval
        timestamp = time.time()
        result = hashgenerator(data + previous_hash + str(timestamp), self.difficulty)
        # Create a new block with the obtained hash and nonce
        block = Block(data, self.chain[-1].index + 1, result[1], timestamp, previous_hash, result[0])
        self.chain.append(block)  # Add the new block to the chain

    def validateBlockchain(self):

        for i in range(1, len(self.chain)):

            val = self.chain[i].vote + self.chain[i].previous_hash + str(self.chain[i].timestamp) + str(self.chain[i].nonce)

            if self.chain[i].hashval != hashfunc(val):
                print(str(i) + " is not a valid block")
                break

        else:
            print("blockchain is valid")


if __name__ == '__main__':
    print("this is the implementation of the blockchain")
