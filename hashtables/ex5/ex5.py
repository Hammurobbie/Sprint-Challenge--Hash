def finder(files, queries):

    result = []
    cache = {}

    for i in files:
        if i in cache:
            pass
        else:
            cache[i] = i
    for i in files:
        for j in queries:
            if j in i:
                result.append(i)

    print(cache)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
