#!/usr/bin/env python

import sys
import os

direc = 'figs/'
files = next(os.walk(direc))

for f in files[2]:
    split = f.split('_')
    if len(split) > 1:
        if 1 < len(split[0]):
            num = int(split[0])
            new_name = "{}{:06d}_{}".format(direc, num, split[1:])
            # print(new_name)
            os.rename("{}{}".format(direc, f), new_name)

