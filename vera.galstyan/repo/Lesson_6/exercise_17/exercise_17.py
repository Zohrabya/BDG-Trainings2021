#!usr\bin\env python 3
import re

tests = [
    'x1bcAd',
    'xAbcd1d',
    'abcde',
    '1234',
    'AAAA'
]

for test in tests:
    m = re.match(r'^(?=[^A-Z] * [A-Z])(?=[^0-9]*[0-9])', test)
    print(test, 'Passed' if m else 'Failed')