"""
Cryptopal challenge 8
"""
import sys
import codecs

search_db = list()
with open(sys.argv[1], 'r') as input_fp:
    for line in input_fp:
        search_db.append(codecs.decode(line.rstrip(), "hex"))
input_fp.close()

for index in range(0, len(search_db)):
    src_ct_line = search_db[index]
    for blk_idx in range(0, len(src_ct_line), 16):
        for test_idx in range(blk_idx+16, len(src_ct_line), 16):
            if (src_ct_line[blk_idx:blk_idx+16] == src_ct_line[test_idx:test_idx+16]):
                print("MATCH : ", index, src_ct_line[blk_idx:blk_idx+16])
                exit()
