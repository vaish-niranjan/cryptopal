"""
Cryptopal challenge 23
"""
import sys
import codecs
import time
import numpy as np
import std_pkg.utils.common as uc
import std_pkg.primitives.MT199937_class as MT199937_class


### 32-bit MT199937 parameters ###
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
u = 11
s = 7
b = 0x9D2C5680
t = 15
c = 0xEFC60000
l = 18

param_hash = {}
param_hash['w'] = w
param_hash['n'] = n
param_hash['m'] = m
param_hash['r'] = r
param_hash['a'] = a
param_hash['b'] = b
param_hash['c'] = c
param_hash['u'] = u
param_hash['l'] = l
param_hash['s'] = s
param_hash['t'] = t

mt_inst = MT199937_class.MT199937(param_hash)
seed = int(time.time()) - np.random.randint(80,2000)
print("seed: ", seed)
mt_inst.seedgen(seed)

mt_state_array = []
gold_randint_array = []
for idx in range(n):
    gold_randint = mt_inst.genrand()
    gold_randint_array.append(gold_randint)
    mt_state_array.append(mt_inst.untamper(gold_randint))

for mti_dup in range(n):
    y = mt_state_array[mti_dup]
    y ^= (y>>u)
    y ^= ((y<<s) & b)
    y ^= ((y<<t) & c)
    y ^= (y>>l) & 0xffffffff   # for 32-bit, masking with 0xffffffff
    if (y != gold_randint_array[mti_dup]):
        print("ERROR: number mismatch at index ", mti_dup, y, gold_randint_array[mti_dup])

print("All matching - final numbers: ", y, gold_randint_array[mti_dup])
