"""
Cryptopal challenge 6
"""
import sys
import codecs
import std_pkg.utils.common as uc

"""
get blocks starting from index 'start_idx' with spacing of keysize 'ksize'
"""
def get_block_idx(data_in, ksize, start_idx):
    new_blk = []
    num_blocks = len(data_in) // ksize
    for idx in range(num_blocks):
        new_blk.append(data_in[start_idx+idx*ksize])
    return new_blk

with open(sys.argv[1], "rb") as data_in_fp:
    #print(uc.hamming_distance(str1, str2))
    data_in = codecs.decode(data_in_fp.read().rstrip(), "base64")

hamming_hash = {}
for ksize in range(2, 41):
    h_distance = 0
    num_blocks = len(data_in) // (2*ksize)
    for idx in range(num_blocks):
        blk_1 = data_in[(idx+0)*ksize:(idx+1)*ksize]
        blk_2 = data_in[(idx+1)*ksize:(idx+2)*ksize]
        h_distance += (uc.hamming_distance(blk_1, blk_2) / ksize)
    hamming_hash[ksize] = (h_distance / num_blocks)

sorted_hamming_hash = {k: v for k, v in sorted(hamming_hash.items(), key=lambda item: item[1])}
keys_array = list(sorted_hamming_hash.keys())

final_str = [']' for x in range(len(data_in))]
num_trials = 1
for guess_key_len in keys_array[0:num_trials]:
    num_blocks = len(data_in) // guess_key_len
    for idx in range(guess_key_len):
        test_blk = get_block_idx(data_in, guess_key_len, idx)
        (score_idx, key_idx, tmp_str) = uc.one_byte_xor_cipher(test_blk)
        for w_idx in range(num_blocks):
            final_str[idx+w_idx*guess_key_len] = tmp_str[w_idx]

print("".join(final_str))
print(len(data_in) % guess_key_len)   ### number of characters missing
