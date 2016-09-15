#!/usr/bin/env python

def replicate_iter(times, data):
    if times <= 0:
        return []
    if not isinstance(data, (int, str)) or not isinstance(times, int):
        raise ValueError
    return [data for i in xrange(times)]

def replicate_recur(times, data):
    if times <= 0:
        return []
    if not isinstance(data, (int, str)) or not isinstance(times, int):
        raise ValueError
    if times != 1:
        return [data] + replicate_recur(times - 1, data)
    else:
        return [data]

if __name__ == '__main__':
    print replicate_iter(3, 'str')
    print replicate_recur(3, 'str')
