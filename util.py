#! /usr/bin/python
# -*- encoding: utf-8 -*-

import hashlib
import random
import hmac
import json
import urllib


conf = json.load(open('trader_cj.conf', 'r'))


def gen_signature(**kargs):
    encode_args = urllib.urlencode(kargs)
    print 'encode_args', encode_args
    pri_key = conf['pri_key']
    mm = hashlib.md5()
    mm.update(pri_key)
    pri_key_md5 = mm.hexdigest()
    return hmac.new(pri_key_md5, encode_args, hashlib.sha256).hexdigest()


def gen_nonce(lens):
    return ''.join([str(random.randint(0, 9)) for i in range(lens)])


if __name__ == '__main__':
    sig2 = gen_signature(price=10000, amount=1, type='buy',
                        key='5zi7w-4mnes-swmc4-egg9b-f2iqw-396z4-g541b',
                        nonce=141377098123)
    print 'sig bb2', sig2
    # print gen_nonce(12)
