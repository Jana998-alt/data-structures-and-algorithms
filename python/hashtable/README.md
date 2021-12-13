# Hashtables
Hash tables are data structures that make it fast to retrive data. it uses a hash function to determine where the data should be placed.

## Challenge
Implement a hash table with 4 methods: add, get, hash, and contains

## Approach & Efficiency
I used the already there hash function from pytho, and made a hash table class of 100 slot-array.
The big O of adding a value is O(1)
the Big O of retriving data varies depending on the data there, but it should be less than O(n)

## API
- add
Arguments: key, value
Returns: nothing
This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
- get
Arguments: key
Returns: Value associated with that key in the table
- contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
- hash
Arguments: key
Returns: Index in the collection for that key
