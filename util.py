#! /usr/bin/python
# -*- encoding: utf-8 -*-

import hashlib
import random
import hmac
import json


conf = json.loads('trader_cj.conf')


def gen_signature(**kargs):
    order=['amount', 'price', 'type', 'nonce', 'key']
    # args_str = reduce(lambda x, y: x + '&' + y,
    #                   map(lambda x: str(x), kargs.values()), '')
    pri_key = conf['pri_key']
    mm = hashlib.md5()
    mm.update(pri_key)
    pri_key_md5 = mm.hexdigest()
    args_str = ''
    for kk in order:
        if kk in kargs:
            args_str = args_str + '&' + str(kargs.get(kk))
    args_str = args_str[1:]
    print 'ttt', hashlib.sha256(args_str).hexdigest()
    print 'ttt2', hmac.new('ooo', args_str, hashlib.sha256).hexdigest()
    print 'ttt3', hmac.new(pri_key_md5, args_str, hashlib.sha256).hexdigest()
    return hmac.new(pri_key_md5, args_str, hashlib.sha256).hexdigest()


def gen_signature2(**kargs):
    v_args = kargs.values()
    print 'v_args', v_args
    v_args = sorted(v_args)
    print 'sort v_args', v_args
    args_str = reduce(lambda x, y: str(x) + '&' + str(y), v_args, '')
    pri_key = 'gNhAK-f@WY}-G[D3h-/CppD-k,A]g-EX{NP-3;iji}'
    mm = hashlib.md5()
    mm.update(pri_key)
    pri_key_md5 = mm.hexdigest()
    return hmac.new(pri_key_md5, args_str, hashlib.sha256).hexdigest()


def gen_nonce(lens):
    return ''.join([str(random.randint(0, 9)) for i in range(lens)])


if __name__ == '__main__':
    sig = gen_signature(price=10000, amount=1, type='buy',
                        key='5zi7w-4mnes-swmc4-egg9b-f2iqw-396z4-g541b',
                        nonce=141377098123)
    sig2 = gen_signature2(price=10000, amount=1, type='buy',
                        key='5zi7w-4mnes-swmc4-egg9b-f2iqw-396z4-g541b',
                        nonce=141377098123)
    print 'sig bb', sig
    print 'sig bb2', sig2
    # print gen_nonce(12)
