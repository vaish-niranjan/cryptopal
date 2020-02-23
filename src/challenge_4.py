"""
Cryptopal challenge 4
"""
import sys
import codecs
import std_pkg.utils.common as uc

str1_fp = open(sys.argv[1], "r")

max_score = 0
final_key = None
final_str = None
for str_line in str1_fp:
    str1_hex = codecs.decode(str_line.rstrip(), 'hex')
    (str_score, key, out_str) = uc.one_byte_xor_cipher(str1_hex)
    if (str_score > max_score):
        max_score = str_score
        final_key = key
        final_str = out_str

print("key is: ", final_key)
print("plaintext is: ", final_str)
