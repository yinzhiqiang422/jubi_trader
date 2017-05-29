#! /usr/bin/python
# -*- encoding: utf-8 -*-

import requests
import json
import time
from util import gen_signature, gen_nonce, gen_signature2


base_url = 'https://www.jubi.com'


def get_stream_ticker(coin):
    param = {'coin': coin}
    url = base_url + '/api/v1/ticker/'
    req = requests.get(url, data=param)
    print type(json.loads(req.content))
    return req.content


def get_depth(coin):
    param = {'coin': coin}
    url = base_url + '/api/v1/depth/'
    req = requests.get(url, data=param)
    return json.loads(req.content)


def get_orders(coin):
    param = {'coin': coin}
    url = base_url + '/api/v1/orders/'
    req = requests.get(url, data=param)
    return json.loads(req.content)


def get_balance(key):
    url = base_url + '/api/v1/balance/'
    # pub_key = 'a3yg3-q28yz-e6j1s-1kifd-f3f1y-iyid2-yp4w6'
    nonce = int(time.time() * 100)
    signature = gen_signature2(nonce=nonce, key=key)
    param = {'key': key, 'nonce': nonce, 'signature': signature}
    req = requests.post(url, data=param)
    return json.loads(req.content)


if __name__ == '__main__':
    # print get_stream_ticker('btc')
    # print get_depth('btc')
    # print get_orders('btc')
    conf = json.load(open('trader_cj.conf', 'r'))
    print get_balance(conf['pub_key'])
