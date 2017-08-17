#! /usr/bin/python
# -*- encoding: utf-8 -*-

import requests
import json
import time
from util import gen_signature, gen_nonce



class JubiTrader(object):
    def __init__(self, f_conf):
        self.conf = json.load(open(f_conf, 'r'))
        self.base_url = 'https://www.jubi.com'

    def get_stream_ticker(self, coin):
        param = {'coin': coin}
        url = self.base_url + '/api/v1/ticker/'
        req = requests.get(url, data=param)
        print type(json.loads(req.content))
        return json.loads(req.content)

    def get_depth(self, coin):
        param = {'coin': coin}
        url = self.base_url + '/api/v1/depth/'
        req = requests.get(url, data=param)
        return json.loads(req.content)

    def get_orders(self, coin):
        param = {'coin': coin}
        url = self.base_url + '/api/v1/orders/'
        req = requests.get(url, data=param)
        return json.loads(req.content)

    def get_balance(self):
        url = self.base_url + '/api/v1/balance/'
        # pub_key = 'a3yg3-q28yz-e6j1s-1kifd-f3f1y-iyid2-yp4w6'
        nonce = int(time.time() * 100)
        signature = gen_signature(nonce=nonce, key=self.conf['pub_key'])
        param = {'key': self.conf['pub_key'], 'nonce': nonce,
                 'signature': signature}
        req = requests.post(url, data=param)
        return json.loads(req.content)

    def get_trade_list(self, coin):
        url = self.base_url + '/api/v1/trade_list/'
        nonce = int(time.time() * 100)
        param = {'key': self.conf['pub_key'], 'nonce': nonce,
                 'coin': coin, 'type': 'all'}
        signature = gen_signature(key=self.conf['pub_key'], nonce=nonce,
                                  coin=coin, type='all')
        param.update({'signature': signature})
        req = requests.post(url, data=param)
        return json.loads(req.content)

    def get_trade_view(self, coin, trade_id):
        url = self.base_url + '/api/v1/trade_view/'
        nonce = int(time.time() * 100)
        signature = gen_signature(key=self.conf['pub_key'], nonce=nonce,
                                  id=trade_id, coin=coin)
        param = {'key': self.conf['pub_key'], 'nonce': nonce,
                 'coin': coin, 'id': trade_id, 'signature': signature}
        req = requests.post(url, data=param)
        return json.loads(req.content)

    def trade_cance(self, coin, trade_id):
        url = self.base_url + '/api/v1/trade_cancel/'
        nonce = int(time.time() * 100)
        signature = gen_signature(key=self.conf['pub_key'], nonce=nonce,
                                  id=trade_id, coin=coin)
        param = {'key': self.conf['pub_key'], 'nonce': nonce,
                 'coin': coin, 'id': trade_id, 'signature': signature}
        req = requests.post(url, data=param)
        return json.loads(req.content)

    def trade_add(self, coin, trade_type, amount, price):
        url = self.base_url + '/api/v1/trade_add/'
        nonce = int(time.time() * 100)
        signature = gen_signature(key=self.conf['pub_key'], nonce=nonce,
                                  type=trade_type, coin=coin, amount=amount,
                                  price=price)
        param = {'key': self.conf['pub_key'], 'nonce': nonce, 'type': trade_type,
                 'coin': coin, 'amount': amount, 'price': price, 'signature': signature}
        req = requests.post(url, data=param)
        return json.loads(req.content)


if __name__ == '__main__':
    trader = JubiTrader('trader_cj.conf')
    # print trader.get_stream_ticker('ifc')
    # print trader.get_orders('btc')
    # print trader.get_balance()
    # print trader.get_trade_list('ifc')
    print trader.trade_add('act', 'buy', 10000, 1.6)
    # print trader.trade_add('ifc', 'sell', 100000, 2.3)
    # print trader.get_trade_view('ifc', '1211470')
    # print trader.trade_cance('ifc', '1211470')
