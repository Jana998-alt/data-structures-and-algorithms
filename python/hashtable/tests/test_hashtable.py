from hashtable import __version__
import pytest
from hashtable.hashtable import Hashtable

def test_version():
    assert __version__ == '0.1.0'

# Adding a key/value to your hashtable results in the value being in the data structure

def test_add_value(table,hash_table):
  key = "Jana"
  value = 23
  acutal = hash_table.add(key, value)
  expected = table[hash(key) % 100]
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

def test_handle_null_retrive():
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
  same_hash = hash_table.hash("Jana")
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
  same_hash = hash_table.hash("Jana")
  key2 = same_hash
  value2 = 'collision'
  hash_table.add(key, value)
  hash_table.add(key2, value2)

  expected = 'collision'
  acutal = hash_table.get(key2)

  expected2 = 23
  acutal2 = hash_table.get("Jana")

  assert expected == acutal, expected2 == acutal2

@pytest.fixture
def table():
  table = []
  for i in range(100):
    table.append([])

@pytest.fixture
def hash_table():
  hash_table = Hashtable()

# sdgkmlsdkf
