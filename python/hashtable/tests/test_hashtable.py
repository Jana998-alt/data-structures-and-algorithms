from hashtable import __version__
import pytest
from hashtable.hashtable import Hashtable, left_join

def test_version():
    assert __version__ == '0.1.0'

# Adding a key/value to your hashtable results in the value being in the data structure

def test_add_value(table,hash_table):
  key = "Jana"
  value = 23
  hash_table.add(key, value)
  acutal = hash_table.__str__()
  expected = "[('Jana', 23)]"
  assert expected == acutal

# Retrieving based on a key returns the value stored

def test_retrive_value(table,hash_table):
  key = "Jana"
  value = 23
  hash_table.add(key, value)
  expected = 23
  acutal = hash_table.get("Jana")
  assert expected == acutal

# Successfully returns null for a key that does not exist in the hashtable

def test_handle_null_retrive(hash_table):
  key = "Jana"
  value = 23
  hash_table.add(key, value)
  expected = None
  acutal = hash_table.get("jana")
  assert expected == acutal

# Successfully handle a collision within the hashtable

def test_collision(table,hash_table):
  key = "Jana"
  value = 23
  same_hash = hash_table._hash("Jana")
  key2 = same_hash
  value2 = 'collision'
  hash_table.add(key, value)
  hash_table.add(key2, value2)
  expected = 2
  acutal = hash_table.table[len(same_hash)]
  assert expected == acutal

# Successfully retrieve a value from a bucket within the hashtable that has a collision

def test_collision(table,hash_table):
  key = "Jana"
  value = 23
  same_hash = hash_table._hash("Jana")
  key2 = same_hash
  value2 = 'collision'
  hash_table.add(key, value)
  hash_table.add(key2, value2)

  expected = 'collision'
  acutal = hash_table.get(key2)

  expected2 = 23
  acutal2 = hash_table.get("Jana")

  assert expected == acutal, expected2 == acutal2

def test_left_join(hash_left_join_table,hash_left_join_table2):
  excepted = [('jana', [23, 1000]), ('potato', [3000, None]), ('kaka', [1000, None]), ('bell', [25, 2000])]
  actual = left_join(hash_left_join_table,hash_left_join_table2)
  for x in excepted:
    for y in actual:
      if x[0][0] == y[0][0]:
        assert x[0][1] == y[0][1]

  assert len(excepted) == len(actual)

@pytest.fixture
def table():
  table = []
  for i in range(100):
    table.append([])
  return table

@pytest.fixture
def hash_table():
  hash_table = Hashtable()
  return hash_table

@pytest.fixture
def hash_left_join_table():
  hash_table = Hashtable()
  hash_table.add("jana",23)
  hash_table.add('bell', 25)
  hash_table.add('potato', 2000)
  return hash_table

@pytest.fixture
def hash_left_join_table2():
  hash_table2 = Hashtable()
  hash_table2.add('jana',1000)
  hash_table2.add('bell', 2000)
  hash_table2.add('kaka',3000)
  return hash_table2

# sdgkmlsdkf
