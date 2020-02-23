"""
Cryptopal challenge 3
"""
import sys
import codecs
import std_pkg.utils.common as uc

str1 = sys.argv[1]
str1_hex = codecs.decode(str1, 'hex')

(str_score, key, out_str) = uc.one_byte_xor_cipher(str1_hex)

print("key is: ", key)
print("plaintext is: ", out_str)
