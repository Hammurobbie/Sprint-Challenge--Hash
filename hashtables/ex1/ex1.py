def get_indices_of_item_weights(weights, length, limit):
    cache = dict()
    # cache = {}
    for i in weights:
        cache[i] = weights.index(i)
        print(weights.index(i))

    for i in range(length):
        if limit - weights[i] in cache:
            print(cache)
            return sorted((i, cache[limit - weights[i]]), reverse=True)
    return None

    # for i in weights:
    #     for j in weights:
    #         if i + j == limit:
    #             return sorted((weights.index(i), weights.index(j)), reverse=True)


get_indices_of_item_weights([5, 4, 2, 16], 4, 20)
get_indices_of_item_weights([4, 4], 2, 8)
