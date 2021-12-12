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

# hash
# Arguments: key
# Returns: Index in the collection for that key

  def _hash(self,key):
    hash_val = hash(key)
    hash_val = hash_val%len(self.table)

    return hash_val


# finds the first word to occur more than once in a string
def repeated_word(string):
  list_words = Hashtable()
  temp_word = ''
  for i in string:
    i = i.lower()
    if i != ' ' and i != '.' and i != ',':
      temp_word = temp_word + i
    else:
      if list_words.contains(temp_word):
        return temp_word
      else:
        if temp_word != '':
          list_words.add(temp_word,1)
          temp_word = ''
  return None
