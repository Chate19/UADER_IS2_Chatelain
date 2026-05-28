# uncompyle6 / decompyle3 - decompilación manual via dis
# Python bytecode version base 3.12.0 (3531)
# Embedded file name: getJason.py
# Compiled at: 2025-05-06 19:05:36
# Size of source mod 2**32: 170 bytes

import json
import sys

jsonfile = sys.argv[1]          # toma el nombre de archivo desde argv[1]
jsonkey = 'token1'              # clave hardcodeada, nunca usada como parámetro

with open(jsonfile, 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)
print(str(obj[jsonkey]))
