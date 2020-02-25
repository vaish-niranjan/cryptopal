"""
Cryptopal challenge 10
"""
import sys
import codecs
import std_pkg.utils.common as uc
import std_pkg.primitives.aes_class as aes_class

with open(sys.argv[1], "rb") as input_fp:
    ct_in_buf = codecs.decode(input_fp.read().rstrip(), "base64")
    key_bytes  = bytearray(map(ord, sys.argv[2]))
    aes_inst = aes_class.AES(key_bytes)
    pt_out_bytes = aes_inst.decrypt_cbc(ct_in_buf, b'0000000000000000')
    pt_out_int = [int.from_bytes(val, "big") for val in pt_out_bytes]
    pt_out_str = list(map(chr, pt_out_int))
    print("".join(pt_out_str))
