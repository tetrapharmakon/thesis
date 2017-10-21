#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import fileinput
import re
 

output = open('clean-hypens.hyph', 'w')
for line in fileinput.input():
    line = re.sub('\[\d*\]','', line.rstrip())
    print(line)
    print >>output, line