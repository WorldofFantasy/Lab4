from Gens import gen_random
from iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'b', 'B']

# Реализация задания 2

for element in Unique(data1):
    print(element, end=' ')

print('\n')

for element in Unique(list(data2)):
    print(element, end=' ')

print('\n')

for element in Unique(list(data3)):
    print(element, end=' ')

print('\n')

for element in Unique(list(data3), ignore_case=True):
    print(element, end=' ')