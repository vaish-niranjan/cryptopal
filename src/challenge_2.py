"""
Cryptopal challenge 2
"""
import sys
import codecs
import std_pkg.utils.common as uc

str1 = sys.argv[1]
str2 = sys.argv[2]

str1_hex = codecs.decode(str1, 'hex')
str2_hex = codecs.decode(str2, 'hex')

str_xor = uc.xor_bytes(str1_hex, str2_hex)

str_xor_hex_enc = codecs.encode(str_xor, 'hex').decode()
print(str_xor_hex_enc)
