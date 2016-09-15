#!/usr/bin/env python

"""
Tax Calculation
- 0 on the first 1000
- 10% on the next 9000
- 15% on the next 10200
- 20% on the next 10550
- 25% on the next 19250
- 30% on the balance
"""

# We can create a list for the % tax and another list for the income segments
# and zip-interate over both to the length of the income segment list while 
# calculating the tax figure and adding them.
# e.g. [0, .1, .15, .2, .25, .3] and [1000, 9000, 10200, 0, 0, 0]

def calculate_tax(income_obj):
    if income_obj == {}:
        return {}
        
    if isinstance(income_obj, int):
        raise ValueError('Invalid input of type int not allowed')

    tax_obj = {}
    for k, v in income_obj.iteritems():
        tax_obj[k] = compute_tax(segment_income(v))
    return tax_obj

def compute_tax(segments):
    tax = 0
    tax_rate = [0, .1, .15, .2, .25, .3]
    for a, b in zip(tax_rate, segments):
        if not isinstance(b, int):
            raise ValueError('Allow only numeric input')
        tax = tax + (a * b)
    return tax

def compute_segment(income, segment):
    if income > segment or income == segment:
        return segment
    else:
        if income < 0:
            return 0
        return income

def segment_income(income):
    income_segments = []

    income_segments.append(compute_segment(income, 1000))
    income_segments.append(compute_segment(income - 1000, 9000))
    income_segments.append(compute_segment(income - 10000, 10200))
    income_segments.append(compute_segment(income - 20200, 10550))
    income_segments.append(compute_segment(income - 30750, 19250))

    balance = income - 50000
    if balance < 0 or balance == 0:
        income_segments.append(0)
    else:
        income_segments.append(income - 50000)

    return income_segments

if __name__ == "__main__":
    # print calculate_tax({'James': 1500})
    print calculate_tax({'Alex': 500, 'James': 20500, 'Kinuthia': 70000})
    # print segment_income(20500)
    # print compute_tax([1000, 9000, 10200, 10550, 19250, 20000])
