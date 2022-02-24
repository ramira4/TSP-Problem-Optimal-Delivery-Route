# get_hash returns hash key given a key (package id number)
def get_hash(key):
    return key % 10


class Hashtable:
    # initiate a hashtable with size 10
    def __init__(self, initial_capacity=10):
        self.map = [[] for i in range(initial_capacity)]

    # insert a key, value pair into hashtable array corresponding to hash key
    def insert(self, key, value):
        hash_key = get_hash(key)
        self.map[hash_key].append([key, value])

    # update a key, value pair in the hash table by finding existing pair and modifying the value
    def update(self, key, value):
        hash_key = get_hash(key)
        for x in self.map[hash_key]:
            if x[0] == key:
                x[1] == value

    # get_value_by_key finds value given a key in hashtable
    def get_value_by_key(self, key):
        hash_key = get_hash(key)
        for x in self.map[hash_key]:
            if x[0] == key:
                return x[1]

    # return and print all 40 packages in hash table by using the get_value_by_key function
    def print_hash(self):
        for i in range(1, 41):
            value = self.get_value_by_key(i)
            print("Package ID #: %s | Delivery Address: %s | Delivery Deadline: %s | City: %s Zip: %s | Weight: %s | Delivery Status: %s" % (value[0], value[3], value[7], value[4], value[6], value[8], value[1]))

