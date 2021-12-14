# Implement a Hashtable Class with the following methods:

class Hashtable():
  def __init__(self):
    self.table = []
    for i in range(100):
      self.table.append([])


# add
# Arguments: key, value
# Returns: nothing
# This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

  def add(self,key, value):
    hash_val = self._hash(key)
    if len(self.table[hash_val]) == 0 :
      self.table[hash_val].append((key, value))
    else:
      for i in self.table[hash_val]:
        if i[0] != key:
          self.table[hash_val] = None
          self.table[hash_val] = (key, value)
        else:
          self.table[hash_val].append((key, value))



# get
# Arguments: key
# Returns: Value associated with that key in the table

  def get(self,key):
    hash_val = self._hash(key)
    for tuple in self.table[hash_val]:
      if tuple[0] == key:
        return tuple[1]
    return None

# contains
# Arguments: key
# Returns: Boolean, indicating if the key exists in the table already.

  def contains(self,key):
    hash_val = self._hash(key)
    for tuple in self.table[hash_val]:
      if tuple[0] == key:
        return True
    return False

  def __iter__(self):
    pass


# hash
# Arguments: key
# Returns: Index in the collection for that key

  def _hash(self,key):
    hash_val = hash(key)
    hash_val = hash_val%len(self.table)

    return hash_val


if __name__ =="__main__":
  key = "jana"
  value = 23
  hash_table = Hashtable()
  print(hash_table._hash(10))
  print(hash_table._hash(20))
  print(hash_table._hash('jana'))
