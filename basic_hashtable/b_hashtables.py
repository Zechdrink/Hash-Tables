

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_pair = None
    
    def __repr__(self):
        return f"({self.key}: {self.value})"

# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.list = None
    



# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashed = 5381
    for x in string:
        hashed = ((hashed << 5) + hashed) + ord(x)
    return hashed % (max - 1)
# << left shift binary operator 

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    key_value_pair = Pair(key, value)
    hashed_index = hash(key_value_pair.key, hash_table.capacity)
    if hash_table.storage[hashed_index] is not None:
        print(f"Overwriting index {hashed_index} of hash table.")
    hash_table.storage[hashed_index] = key_value_pair
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
    # if hash_table.list[key_hash] is not None:
    #     return hash_table.list[key_hash].value
    if hash_table.storage[key_hash] is not None:
        if hash_table.list is not None:
            if hash_table.list[key_hash is not None]:
                return hash_table.list[key_hash].value
        else:
            return hash_table.storage[key_hash].value
    else:
        return None

def storage_double(hash_table):
    new_capacity = hash_table.capacity * 2
    new_elements = [None] * new_capacity

    # Copy over elements
    for i in range(len(hash_table.storage)):
        if hash_table.storage[i] is not None:
            new_elements[i] = hash_table.storage[i]

    hash_table.storage = new_elements
    hash_table.capacity = new_capacity


def Testing():
    ht = BasicHashTable(4)

    hash_table_insert(ht, "live", "Here today...\n")
    hash_table_insert(ht, "b", "Here today...\n")
    hash_table_insert(ht, "c", "Here today...\n")
    hash_table_insert(ht, "d", "Here today...\n")
    hash_table_insert(ht, "e", "Here today...\n")
    hash_table_insert(ht, "f", "Here today...\n")
    hash_table_insert(ht, "g", "Here today...\n")
    hash_table_insert(ht, "h", "Here today...\n")


    # hash_table_remove(ht, "line")

    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")

    print(ht.storage, ht.capacity, "\n")
    print(ht.list, "list")
    storage_double(ht)
    print(ht.storage, ht.capacity, "\n")
    print(ht.storage[1])


Testing()
