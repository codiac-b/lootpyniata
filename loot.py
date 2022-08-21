import logging
class Loot:
    """
    Creates an item of loot.

    Attributes
    __________
        item_id : int
            wowhead item id
        item_name : str
            Item name.
        item_source : str
            Item source. Who drops this item.
        drop_chance : float
            Percent chance an item will be dropped. 0 - 1.

    """

    def __init__(self, item_id, item_name, item_source, drop_chance):
        self.item_id = item_id
        self.item_name = item_name
        self.item_source = item_source
        self.drop_chance = drop_chance
        self.cume_drop_chance = None

    def __repr__(self):
        return f'Loot({self.item_id=}, {self.item_name=}, {self.item_source=}, {self.drop_chance=}, {self.cume_drop_chance=})'

    # Validate attributes
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        try:
            self._item_id = int(value)
            logging.debug('Validated item_id')
        except ValueError:
            raise ValueError('item_id must be a float') from None

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        try:
            self._item_name = str(value)
            logging.debug('Validated item_name')
        except ValueError:
            raise ValueError('item_name must be a string') from None

    @property
    def item_source(self):
        return self._item_source

    @item_source.setter
    def item_source(self, value):
        try:
            self._item_source = str(value)
            logging.debug('Validated item_source')
        except ValueError:
            raise ValueError('item_source must be a string') from None

    @property
    def drop_chance(self):
        return self._drop_chance

    @drop_chance.setter
    def drop_chance(self, value):
        if 0 <= float(value) <= 1:
            try:
                self._drop_chance = float(value)
                logging.debug('Validated drop_chance')
            except TypeError:
                raise TypeError('drop_chance must be a float') from None
        else:
            raise ValueError('drop_chance must be between 0 and 1, inclusive.') from None

