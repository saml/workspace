import itertools
import io


def split_at(iterable, n):
    '''returns two iterables: first n elements and the rest'''
    env = {'count':0}
    def keyfunc(x):
        env['count'] += 1
        return env['count'] <= n

    groups = itertools.groupby(iterable, keyfunc)
    return next(groups)[1],next(groups)[1]

if __name__ == '__main__':
    data = io.BytesIO(bytes('1234567890'))
    head,tail = split_at(iter(lambda: data.read(1),"") ,3)

    print('|'.join((','.join(tail), ','.join(head))))
