def has_negatives(a):
    cache = {}
    result = []

    for num in a:
        if abs(num) in cache:
            cache[abs(num)] = 1
            result.append(abs(num))
        else:
            cache[abs(num)] = 0

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
