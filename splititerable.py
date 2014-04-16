from StringIO import StringIO
import itertools

def split_at(iterable, n):
    '''returns two iterables: first n elements and the rest'''
    first = itertools.islice(iterable, n)
    rest = itertools.islice(iterable,n,None)
    return first,rest

def protocol(value):
    for x in value:
        yield x

buff = protocol('1234567890')
head,tail = split_at(buff,3)

for x in head:
    print(x)
print('--')
for x in tail:
    print(x)

