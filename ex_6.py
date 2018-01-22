import json
import sys
from Gens import field, gen_random
from decoretors import print_result
from iterators import Unique as unique
from Ctxmnrgs import timer

path = "data_light_cp1251.json"

with open(path) as f:
    data = json.load(f)

def f1(arg):
    return (sorted([i for i in unique([j['job-name'] for j in arg], ignore_case=True)]))

def f2(arg):
    return (filter(lambda x: (x.lower().find('программист') == 0), arg))

def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))

@print_result
def f4(arg):
    return (["{}, {} {} {}".format(x, "зарплата", y, "руб.") for x, y in zip(arg, list(gen_random(100000, 200000, len(arg))))])

with timer():
    f4(f3(f2(f1(data))))