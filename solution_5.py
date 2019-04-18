import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)

    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

block0 = Block('13:12 4/2/2019', "Some Information", 0)
block1 = Block('13:12 4/2/2019', "Another Information", block0)
block2 = Block('13:12 4/2/2019', "Some more Information", block1)

print(block0.data)
print(block0.hash)
print(block1.previous_hash.data)
