# -*- coding: utf-8 -*-
from items import *

def default_factory(item_name): 
    if   item_name == AGED_BRIE     : return update_aged_brie
    elif item_name == SULFURAS      : return update_sulfuras
    elif item_name == BACKSTAGE_PASS: return update_backstage_pass
    elif item_name == CONJURED_CAKE : return update_conjured_cake
    else                            : return update_normal_item

def update_normal_item(sell_in, quality):
    return (sell_default_update(sell_in), Quality.floor(quality - normal_delta(sell_in)))

def update_aged_brie(sell_in, quality):
    return (sell_default_update(sell_in), Quality.ceil(quality + normal_delta(sell_in)))

def update_sulfuras(sell_in, quality):
    return (sell_in, quality)

def update_backstage_pass(sell_in, quality): 
    if sell_in <= 0:
        update = lambda _: 0
    else:
        if sell_in <= 5:
            delta = 3
        elif sell_in <= 10:
            delta = 2
        else:
            delta = 1
        update = lambda q: Quality.ceil(q + delta)
    return (sell_default_update(sell_in), update(quality))

def update_conjured_cake(sell_in, quality):
    return (sell_default_update(sell_in), Quality.floor(quality - 2 * normal_delta(sell_in)))

def sell_default_update(value):
    return value - 1

def normal_delta(sell_in):
    return 1 if sell_in > 0 else 2

class Quality:
    @classmethod
    def floor(cls, value):
        return max(0, value)

    @classmethod
    def ceil(cls, value):
        return min(50, value)