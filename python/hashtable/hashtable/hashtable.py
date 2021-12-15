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

  def __iter__(self):
    values_in = []
    for i in range(len(self.table)):
      if len(self.table[i]) == 0:
        pass
      else:
        for j in range(len(self.table[i])):
          values_in.append(self.table[i][j])

    return values_in

  def __str__(self):
    return self.__iter__().__str__()




# Write a function called left join
# Arguments: two hash maps
# The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
# The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
# Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

def left_join(hash1, hash2):
    array_of_values1 = hash1.__iter__()
    array_of_values2 = hash2.__iter__()
    array_answer = Hashtable()

    for i in range(len(array_of_values1)):
      key1 = array_of_values1[i][0]
      value1 = array_of_values1[i][1]
      if hash2.contains(key1):
        value2 = hash2.get(key1)
        array_answer.add(key1, [value1, value2])
      elif not hash2.contains(key1) and not array_answer.contains(key1):
        array_answer.add(key1, [value1, None])


    for i in range(len(array_of_values2)):
      key2 = array_of_values2[i][0]
      value2 = array_of_values2[i][1]
      if not hash1.contains(key2) and not array_answer.contains(key2):
        array_answer.add(key2, [value2, None])

    return array_answer.__iter__()


