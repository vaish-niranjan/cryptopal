"""
Cryptopal challenge 5
"""
import sys
import codecs
import std_pkg.utils.common as uc

str1 = sys.argv[1]
key = list(map(ord, sys.argv[2]))

with open(sys.argv[1], "rb") as str_fp:
    str_buffer = str_fp.read().rstrip()
    key_array = bytearray([key[idx%len(key)] for idx in range(len(str_buffer))])
    str_xor = uc.xor_bytes(str_buffer, key_array)
    str_xor_hex_enc = codecs.encode(str_xor, 'hex').decode()
    print(str_xor_hex_enc)
