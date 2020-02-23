import codecs
import re
import collections

"""
input_str and b64_str are represented in bytes.
"""
def hex_to_base64(input_str):
    b64_str = codecs.encode(codecs.decode(input_str, 'hex'), 'base64').decode()
    return b64_str

"""
str1 and str2 are represented in bytes.
"""
def xor_bytes(str1, str2):
    result = bytearray([(a ^ b) for (a,b) in zip(str1, str2)])
    return result

"""
str1 and str2 are represented in bytes.
"""
def hamming_distance(str1, str2):
    count = 0
    for (a,b) in zip(str1, str2):
        count += bin(a^b).count("1")
    return count

"""
Calculate score of a string: alphabhets+space+newline+tab counts 1, others 0
input_data in bytes
"""
def calc_str_score(input_data):
    alphanum_nt = list(filter(lambda x:(x==10) or (x==9) or (x==32) or ((x>=65) and (x<=90)) or ((x>=97) and (x<=122)), input_data))
    return len(alphanum_nt)

"""
single-byte XOR cipher
input str in bytes
"""
def one_byte_xor_cipher(input_str):
    max_score = 0
    max_score_str = None
    freq_chars = "ETAOINetaoin SHRDLUshrdlu"
    freq_chars_ord = list(map(ord, freq_chars))

    inp_ch_freq = collections.Counter(input_str)
    inp_ch_top2_freq = inp_ch_freq.most_common(2)

    for expected_char in freq_chars_ord:
        for match_pair_idx in range(len(inp_ch_top2_freq)):
            comm_char = inp_ch_top2_freq[match_pair_idx][0]
            exepected_key = comm_char ^ expected_char
            #print(expected_char, match_pair_idx, comm_char, exepected_key)
            key_array = bytearray([exepected_key for idx in range(len(input_str))])
            #print(key_array)
            out_str = xor_bytes(input_str, key_array)
            str_score = calc_str_score(out_str)
            #print("str_score: ", str_score)
            if (str_score > max_score):
                max_score = str_score
                max_score_str = out_str
                final_key = exepected_key
                final_str = "".join(list(map(chr, max_score_str)))
                #print(final_str)

    final_str = "".join(list(map(chr, max_score_str)))
    return (max_score, final_key, final_str)
