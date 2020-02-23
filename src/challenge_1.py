"""
Cryptopal challenge 1
"""
import sys
import std_pkg.utils.common as uc

input_str = sys.argv[1]

b64_str = uc.hex_to_base64(input_str)
print(b64_str)
