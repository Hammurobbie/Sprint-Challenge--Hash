def intersection(arrays):

    cache = {}
    result = []

    for i in range(10):
        if i in arrays[0]:
            cache[i] = 1
    for i in range(len(arrays) - 1):
        if cache[1] in arrays[i]:
            cache[1] += 1
        if cache[2] in arrays[i]:
            cache[2] += 1
        if cache[3] in arrays[i]:
            cache[3] += 1

    for i in cache.items():
        print(i[1])
        if i[1] > 1:
            result.append(i[0])

    print(cache)
    return result


if __name__ == "__main__":
    arrays = [[1, 2, 3],
              [1, 4, 5],
              [1, 6, 7]]

    print(intersection(arrays))
