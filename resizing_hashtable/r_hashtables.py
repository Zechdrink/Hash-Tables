

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"({self.key}: {self.value})"


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
    
    def __repr__(self):
        return f"({self.capacity}: {self.storage})"


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hashed = 5381
    for x in string:
        hashed = ((hashed << 5) + hashed) + ord(x)
    return hashed % (max - 1)

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashed_index = hash(key, hash_table.capacity)
    if hash_table.storage[hashed_index]:
        current = hash_table.storage[hashed_index]
        while current:
            if current.key == key:
                current.value = value
                return
            else:
                if current.next is None:
                    current.next = LinkedPair(key, value)
                current = current.next
    else:
        hash_table.storage[hashed_index] = LinkedPair(key, value)



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_index = hash(key, hash_table.capacity)
    if hash_table.storage[hashed_index]:
        if hash_table.storage[hashed_index].key == key:
            hash_table.storage[hashed_index] = None
        else:
            current = hash_table.storage[hashed_index]
            while current:
                if current.key == key:
                    current = None
                else:
                    current = current.next

    else:
       print("a warning")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    key_hash = hash(key, hash_table.capacity)

    if hash_table.storage[key_hash] is not None:
        if hash_table.storage[key_hash].key == key:
            return hash_table.storage[key_hash].value
        else:
            current = hash_table.storage[key_hash]
            while current:
                if current.key == key:
                    return current.value
                else:
                    current = current.next
            return None
    else:
        print("solo key")
        return None

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2
    new_elements = [None] * new_capacity

    # Copy over elements
    for i in range(len(hash_table.storage)):
        if hash_table.storage[i] is not None:
            new_elements[i] = hash_table.storage[i]

    hash_table.storage = new_elements
    hash_table.capacity = new_capacity
    return hash_table


def Testing():
    ht = HashTable(2)
  
    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
