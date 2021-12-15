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




# Write a function called left join
# Arguments: two hash maps
# The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
# The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
# Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

def left_join(hash1, hash2):
  array_of_values1 = hash1.__iter__()
  array_of_values2 = hash2.__iter__()
  array_answer = []

  for i in range(len(array_of_values1)):
    key1 = array_of_values1[i][0]
    value1 = array_of_values1[i][1]
    exists = 0
    if hash2.contains(key1) and exists ==0:
      for j in range(len(array_of_values1)):
        key2 = array_of_values2[j][0]
        value2 = array_of_values2[j][1]
        if key1 == key2:
          array_answer.append([key1, value1, value2])
          exists = 1
        elif not hash1.contains(key2) and exists ==0:
          array_answer.append([key2, value2, None])
    else:
      array_answer.append([key1, value1, None])

  return array_answer



if __name__ =="__main__":
  key = "jana"
  value = 23
  hash_table = Hashtable()
  hash_table.add(key,value)
  hash_table.add('bell', 25)
  hash_table2 = Hashtable()
  hash_table2.add('jana',1000)
  hash_table2.add('bell', 2000)
  hash_table2.add('kaka',1000)
  hash_table.add('potato', 2000)

  print(left_join(hash_table, hash_table2))

# dgfdgf
