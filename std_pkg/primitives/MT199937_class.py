import sys
import numpy as np
import pandas as pd

class MT199937:
    """
    Mersenne Twister Random Number Generator
    """
    def __init__(self, param_hash):
        self.param_hash = param_hash
        self.w = self.param_hash['w']
        self.n = self.param_hash['n']
        self.m = self.param_hash['m']
        self.r = self.param_hash['r']
        self.a = self.param_hash['a']
        self.b = self.param_hash['b']
        self.c = self.param_hash['c']
        self.u = self.param_hash['u']
        self.l = self.param_hash['l']
        self.s = self.param_hash['s']
        self.t = self.param_hash['t']
        self.mt_state = np.zeros(self.n).astype("int")
        self.mag01 = (0x0, self.a)
        self.mti = self.n + 1
        self.mti_dup = 0

    def print_params(self):
        for key in self.param_hash.keys():
            print(key, hex(self.param_hash[key]))

    def seedgen(self, seed):
        mt_state = self.mt_state
        mt_state[0] = seed & 0xffffffff
        for mti in range(1, self.n):
            mt_state[mti] = (69069 * mt_state[mti-1]) & 0xffffffff
        self.mt_state = mt_state
        self.mti = mti+1

    def genrand(self):
        mti = self.mti
        mt_state = self.mt_state
        if (mti >= self.n):
            if (mti == self.n+1):
                self.seedgen(4357)
            for kk in range(0, self.n-self.m):
                y = (mt_state[kk] & self.u) | (mt_state[kk+1] & self.l)
                mt_state[kk] = mt_state[kk+self.m] ^ (y>>1) ^ self.mag01[y & 0x1]
            for kk in range(self.n-self.m, self.n-1):
                y = (mt_state[kk] & self.u) | (mt_state[kk+1] & self.l)
                mt_state[kk] = mt_state[kk+self.m-self.n] ^ (y>>1) ^ self.mag01[y & 0x1]
            y = (mt_state[self.n-1] & self.u) | (mt_state[0] & self.l)
            mt_state[self.n-1] = mt_state[self.m-1] ^ (y>>1) ^ self.mag01[y & 0x1]
            self.mti = 0
            self.mt_state = mt_state
        y = self.mt_state[self.mti]
        self.mti += 1
        y ^= (y>>self.u)
        y ^= ((y<<self.s) & self.b)
        y ^= ((y<<self.t) & self.c)
        y ^= (y>>self.l) & 0xffffffff   # for 32-bit, masking with 0xffffffff
        return y

    def untamper(self, test_int):
        y = test_int
        y_orig_l = (y >> self.l) ^ (y & (0xffffffff >> self.l))
        y_orig_u = y & (0xffffffff << (self.w - self.l))
        y_4_out = y_orig_u | y_orig_l

        d_mask = self.c
        y_out_new = y_4_out
        mask_s  = 0xffffffff >> (self.w - self.t)
        mask_s_last = 0xffffffff >> (self.w - (self.w % self.t))

        lower_s = (y_4_out & mask_s)
        final_y = lower_s
        for blk_i in range(1, self.w // self.t):
            d_mask = d_mask >> self.t
            y_out_new = y_out_new >> self.t
            lower_s = ((lower_s & d_mask) ^ y_out_new) & mask_s
            final_y = (lower_s << blk_i*self.t) | final_y

        d_mask = d_mask >> self.t
        y_out_new = y_out_new >> self.t
        lower_s = ((lower_s & d_mask) ^ y_out_new) & mask_s_last
        final_y = (lower_s << (blk_i+1)*self.t) | final_y

        d_mask = self.b
        y_out_new = final_y
        mask_s  = 0xffffffff >> (self.w - self.s)
        mask_s_last = 0xffffffff >> (self.w - (self.w % self.s))

        lower_s = (final_y & mask_s)
        final_y = lower_s
        for blk_i in range(1, self.w // self.s):
            d_mask = d_mask >> self.s
            y_out_new = y_out_new >> self.s
            lower_s = ((lower_s & d_mask) ^ y_out_new) & mask_s
            final_y = (lower_s << blk_i*self.s) | final_y

        d_mask = d_mask >> self.s
        y_out_new = y_out_new >> self.s
        lower_s = ((lower_s & d_mask) ^ y_out_new) & mask_s_last
        final_y = (lower_s << (blk_i+1)*self.s) | final_y


        ### generalization needed ###
        y = final_y
        y31_21 = (y & 0xffe00000)
        y20_10 = ((y31_21 >> 11) ^ y) & 0x001ffc00
        y9_0   = ((y20_10 >> 11) ^ y) & 0x000003ff
        final_y = y31_21 | y20_10 | y9_0
        return final_y
