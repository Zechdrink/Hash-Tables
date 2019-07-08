

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_pair = None


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        pass


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashed = 5381
    for x in string:
        hashed = ((hashed << 5) + hashed) + ord(x)
    return hashed % (max - 1)

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    new_pair = Pair(key, value)
    hashed_index = hash(new_pair.key, hash_table.capacity)
    if hash_table.storage[hashed_index] is not None:
        print(f"Overwriting index {hashed_index} of hash table.")

    hash_table.storage[hashed_index] = new_pair
# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):

    hashed_index = hash(key, hash_table.capacity)
    if hash_table.storage[hashed_index]:
        del hash_table.storage[hashed_index]
    else:
       print("a warning")



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    key_hash = hash(key, hash_table.capacity)
    if hash_table.storage[key_hash] is not None:
        return hash_table.storage[key_hash].value
    else:
        return None

def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")
    print(ht, "hereeeeeeeeeeee")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
