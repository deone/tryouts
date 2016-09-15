def pad_digits(integer):
    str_int = str(integer)
    length = len(str_int)
    padded = []

    for i in range(length):
        position = length - (i + 1)
        padding = '0' * position

        val = str_int[i] + padding

        if len(val) > 1 and val not in exceptions.keys():
            result = by_length(val)
        elif val == '0':
            result = None
        else:
            result = val
        
        padded.append(result)

    return padded

def by_length(num):
    length = len(num)
    integer = num[:1]

    divider = '1' + ('0' * (length - 1))

    if integer == '1':
        return divider

    if integer not in ('0', '1'):
        return [integer, divider]

def convert(lst):
    words = ""
    for i in lst:
        if i is not None:
            words += translate(i)
    return words[:-1]

def scan_dict(val):
    if val not in int_dict.keys() and val not in exceptions.keys():
        print "Number not supported"
        return
    else:
        try:
            return int_dict[val]
        except:
            return exceptions[val]

def translate(val):
    if type(val) is str:
        return scan_dict(val) + " "
    else:
        result = ""
        for i in val:
            result += scan_dict(val) + "-"

        return result[:-1] + " "

def main(integer):
    seq = pad_digits(integer)
    return convert(seq)

int_dict = {
            '1': 'ichi',
            '2': 'ni',
            '3': 'san',
            '4': 'yon',
            '5': 'go',
            '6': 'roku',
            '7': 'nana',
            '8': 'hachi',
            '9': 'kyuu',
            '10': 'juu',
            '20': 'ni-juu',
            '30': 'san-juu',
            '100': 'hyaku',
            '1000': 'sen',
            # '10000': 'man',
            '10000': 'ichi-man',
            '100000000': 'oku',
            # '1000000000000': 'chou',
            '1000000000000': 'itchou',
            # '10000000000000000': 'kei',
            '10000000000000000': 'ikkei',
            }

exceptions = {
            '300': 'sanbyaku',
            '600': 'roppyaku',
            '800': 'happyaku',
            '3000': 'sanzen',
            '8000': 'hassen',
            '8000000000000': 'hatchou',
            '10000000000000': 'jutchou',
            '60000000000000000': 'rokkei',
            '80000000000000000': 'hakkei',
            '100000000000000000': 'jukkei',
            '1000000000000000000': 'hyakkei'
        }
