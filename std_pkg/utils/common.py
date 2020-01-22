import codecs
import sys

"""
input_str and b64_str are represented in bytes.
"""
def hex_to_base64(input_str):
    b64_str = codecs.encode(codecs.decode(input_str, 'hex'), 'base64').decode()
    return b64_str
