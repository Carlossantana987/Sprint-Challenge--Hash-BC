#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # here we are inserting in the HT using source a key and destination as value
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)
        # print(hash_table_insert(hashtable, i.source, i.destination))

    # here if find the first ticket which source is None but give us the next destination as value
    destination = hash_table_retrieve(hashtable, "NONE")
    # print(destination)

    for i in range(length):
        # Construct the route
        route[i] = destination
        # getting the next destination
        destination = hash_table_retrieve(hashtable, destination)

    print(route)
    return route
