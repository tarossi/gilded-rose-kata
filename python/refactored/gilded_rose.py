# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items, item_behavior_factory):
        self.items = items
        self.resolve_item_behavior = item_behavior_factory

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        item_behavior = self.resolve_item_behavior(item.name)
        (updated_sell_in, updated_quality) = item_behavior(item.sell_in, item.quality)
        item.sell_in = updated_sell_in
        item.quality = updated_quality

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)