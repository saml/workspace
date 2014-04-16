import itertools
import io

def split_at(iterable, n):
    '''returns two iterables: first n elements and the rest'''
    first = itertools.islice(iterable, n)
    rest = itertools.islice(iterable,n,None)
    return first,rest

data = io.BytesIO(bytes('1234567890'))
head,tail = split_at(iter(lambda: data.read(1),"") ,3)

for x in head:
    print(x)
print('--')
for x in tail:
    print(x)

