def fOnly(n):
    list1_iterator = (filter(lambda x: isinstance(x, int), n))
    print(__name__)
    return list(list1_iterator)

