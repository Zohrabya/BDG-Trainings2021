#!/usr/bin/env python3

import random

lp_3, lp_4 = [], []

def generate_license_plate_3():
    while len(lp_3) < 6:
        if len(lp_3) < 3:
            s = random.randrange(97,123)
            lp_3.append(chr(s).upper())
        else:
            s = random.randrange(0, 9)
            lp_3.append(str(s))
    return lp_3

def generate_license_plate_4():
    while len(lp_4) < 7:
        if len(lp_4) < 4:
            s = random.randrange(97,123)
            lp_4.append(chr(s).upper())
        else:
            s = random.randrange(0, 9)
            lp_4.append(str(s))
    return lp_4

license_plates = ["".join(generate_license_plate_3()), "".join(generate_license_plate_4())]
random.shuffle(license_plates)

print(license_plates[0])
