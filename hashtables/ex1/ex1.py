#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Insert in HT
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    for i in range(length):
        # the item is the diff between the
        # limit (sum we are looking for)
        # and the weight at current index
        item = limit - weights[i]
        # therefore we look for the item(diff) in the HT
        answer = hash_table_retrieve(ht, item)
        # if we found an item we return the answer index
        # and the current index in the loop
        if answer:
            return (answer, i)

    return None








    # #loop through the length
    # for i in range(length):
    #
    #     #check and see each index is greater then limit
    #     if weights[i] < limit:
    #
    #         #if index is less then the limit. Use insert method from hashtables to
    #         hash_table_insert(ht, weights[i], i)
    #
    # #loop through weights with enumerate method
    # for i, w in enumerate(weights):
    #     print(f'weight: {w}')
    #
    #     limits = 0
    #
    #     if limit - w < 0:
    #
    #         limits = w - limit
    #         print(limits)
    #     else:
    #
    #         limits = limits - w
    #
    #         print(limits)
    #
    #     if hash_table_retrieve(ht, limits):
    #
    #         print(hash_table_retrieve(ht, limits))
    #
    #     if w > limits:
    #
    #         return (i, hash_table_retrieve(ht, limits))
    #
    #     else:
    #
    #         return (hash_table_retrieve(ht, limits), i)
    #
    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
