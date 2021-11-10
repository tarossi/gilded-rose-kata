# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose 
from items import *
from item_behavior import default_factory
from copy import deepcopy

class GildedRoseTest(unittest.TestCase):

    def test_normal(self):
        self._test_template(ELIXIR_MONGOOSE, lambda item: [
            (item(sell_in=-1, quality= 0), (-2, 0)),
            (item(sell_in=-1, quality=10), (-2, 8)),
            (item(sell_in= 0, quality=10), (-1, 8)),
            (item(sell_in= 1, quality= 0), ( 0, 0)),
            (item(sell_in= 1, quality=10), ( 0, 9)),
            (item(sell_in= 6, quality=10), ( 5, 9)),
            (item(sell_in=11, quality=10), (10, 9)),
        ])

    def test_sulfuras(self):
        self._test_template(SULFURAS, lambda item: [
            (item(sell_in=-1, quality=80), (-1, 80)),
            (item(sell_in= 0, quality=80), ( 0, 80)),
            (item(sell_in= 1, quality=80), ( 1, 80)),
            (item(sell_in= 6, quality=80), ( 6, 80)),
            (item(sell_in=11, quality=80), (11, 80)),
        ])

    def test_aged_brie(self):
        self._test_template(AGED_BRIE, lambda item: [
            (item(sell_in=-1, quality=49), (-2, 50)),
            (item(sell_in=-1, quality=10), (-2, 12)),
            (item(sell_in= 0, quality=10), (-1, 12)),
            (item(sell_in= 1, quality=50), ( 0, 50)),
            (item(sell_in= 1, quality=10), ( 0, 11)),
            (item(sell_in= 6, quality=10), ( 5, 11)),
            (item(sell_in=11, quality=10), (10, 11)),
        ])

    def test_backstage_pass(self):
        self._test_template(BACKSTAGE_PASS, lambda item: [
            (item(sell_in=-1, quality=50), (-2,  0)),
            (item(sell_in=-1, quality= 0), (-2,  0)),
            (item(sell_in=-1, quality=10), (-2,  0)),
            (item(sell_in= 0, quality=10), (-1,  0)),
            (item(sell_in= 1, quality=48), ( 0, 50)),
            (item(sell_in= 1, quality=10), ( 0, 13)),
            (item(sell_in= 6, quality=10), ( 5, 12)),
            (item(sell_in=11, quality=10), (10, 11)),
        ])

    def test_conjured_cake(self):
        self._test_template(CONJURED_CAKE, lambda item: [
            (item(sell_in=-1, quality= 0), (-2, 0)),
            (item(sell_in=-1, quality=10), (-2, 6)),
            (item(sell_in= 0, quality=10), (-1, 6)),
            (item(sell_in= 1, quality= 0), ( 0, 0)),
            (item(sell_in= 1, quality=10), ( 0, 8)),
            (item(sell_in= 6, quality=10), ( 5, 8)),
            (item(sell_in=11, quality=10), (10, 8)),
        ])

    def _test_template(self, item_name, item_before_after):
        create_item = lambda sell_in, quality: Item(item_name, sell_in, quality)
        (items, expected) = zip(*item_before_after(create_item))
        updated_items = self._update_quality(items)
        self.assertEqual(list(expected), list(map(lambda i: (i.sell_in, i.quality), updated_items)))
    
    def _update_quality(self, items):
        items_copy = deepcopy(items)
        gilded_rose = GildedRose(items_copy, default_factory)
        gilded_rose.update_quality()
        return items_copy
        
if __name__ == '__main__':
    unittest.main()
