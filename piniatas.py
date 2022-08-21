import math
import random
class Piniata:
    """
    All other piniatas inherit from this class.
    They should at least have a loot_table attribute and a 'generate_drop_list' method.
    """
    def __init__(self, loot_table=None):
        self.loot_table = loot_table

# TODO flesh out creature class
# class Creature(Piniata):
#     """
#     Creates a creature with a loot table to sim drops from.
#
#     Attributes
#     __________
#         loot_table : list
#             The list of items a creature can drop. Should use a list of Loot objects.
#         drop_size : int, range
#             The number of items a creature can drop.
#         drop_size_chance : dict, optional
#             The chance a creature will drop a certain number of items.
#         gauranteed_drops : list, optional
#             A list of item gauranteed to drop, potentially with conditions. Not implemented
#
#     """
#     def __init__(self, loot_table, drop_size, gauranteed_drops=None):
#         Piniata.__init__(self, loot_table)
#         self.loot_table = loot_table
#         self.drop_size = drop_size
#         self.gauranteed_drops = gauranteed_drops


class Boss(Piniata):
    """
    Creates a boss with a loot table to sim drops from.

    Attributes
    __________
        name: str
            Name of boss
        tier_dropper : bool, optional
            Set if a boss drops tier pieces. This changes the loot table to guarantee tokens.
        loot_table : list
            The list of items a boss can drop. Should use a list of Loot objects.
        raid_size : int
            Sets raid size. Used to determine number of items dropped. Must be 10 or 25.
    """
    def __init__(self, tier_dropper=False, loot_table=None, raid_size=None, name=None):
        Piniata.__init__(self, loot_table)
        self.name = name
        self.tier_dropper = tier_dropper
        self.loot_table = loot_table
        self.raid_size = raid_size
        # TODO make these configureable
        self.non_tier_loot_size = {25: 4, 10: 2}[self.raid_size]
        self.tier_loot_size = {25: 4, 10: 2}[self.raid_size]

    def generate_drop_list(self):
        # Sort loot_table by item_id
        self.loot_table.sort(key=lambda y: y.item_id)
        dropped_items = []
        for i in range(self.non_tier_loot_size):
            cume_drop_chance_sum = 0
            for item in self.loot_table:
                item.cume_drop_chance = cume_drop_chance_sum + item.drop_chance
                cume_drop_chance_sum = cume_drop_chance_sum + item.drop_chance

            drop_seed = random.uniform(0, self.loot_table[-1].cume_drop_chance)
            for index, item in enumerate(self.loot_table):
                if drop_seed <= item.cume_drop_chance:
                    dropped_items.append(item)
                    self.loot_table.pop(index)
                    break
                else:
                    continue
        return dropped_items
