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


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp

block0 = Block('13:12 4/2/2019', "Some Information", 0)
block1 = Block('13:12 4/2/2019', "Another Information", block0)
block2 = Block('13:12 4/2/2019', "Some more Information", block1)

print(block0.data)
print(block0.hash)
print(block1.previous_hash.data)

temp = LinkedList()
temp.append('13:12 4/2/2019', "Some Information")
temp.append('13:12 4/2/2019', "Another Information")
print(temp.last.data)
print(temp.last.previous_hash.data)
