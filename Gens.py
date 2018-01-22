import random

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            if args[0] in i: yield i[args[0]]
    else:
        for i in items:
            res = {}
            for j in args:
                if j in i:
                    res[j] = i[j]
            yield res


def gen_random(begin, end, num_count):
    for i in range (num_count):
        yield random.randint(begin, end)
