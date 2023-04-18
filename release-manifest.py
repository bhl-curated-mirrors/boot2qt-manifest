#!/bin/env python
# Copyright (C) 2023 The Qt Company Ltd.

import sys
import re
import argparse

parser = argparse.ArgumentParser(
                    prog=sys.argv[0],
                    description='Create release manifest')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

with open(args.input) as inputfile:
    with open(args.output, "w") as outputfile:
        for line in inputfile:
            include = re.search('include name="(.*)"', line)
            if (include):
                with open(include.group(1)) as includeFile:
                    for includeLine in includeFile:
                        if (not includeLine.startswith('<')):
                            outputfile.write(includeLine)
            else:
                outputfile.write(line)
