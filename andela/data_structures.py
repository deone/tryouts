#!/usr/bin/env python

import types

def manipulate_data(lst):
    result = []
    if not isinstance(lst, types.ListType):
        return 'Only lists allowed'

    count_positives = len([x for x in lst if x >= 0])
    if not count_positives:
        result.append(0)
    else:
        result.append(count_positives)

    sum_negatives = sum([x for x in lst if x < 0])
    if not sum_negatives:
        result.append(0)
    else:
        result.append(sum_negatives)

    return result

if __name__ == '__main__':
    print manipulate_data([0, -9, 2, 3, 4, -5])
