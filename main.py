from loot import Loot
from piniatas import Boss
from collections import Counter

def generate_drop_list(enemies):
    """
    Takes a list of Piniatas and sims their drops
    """
    print("Generating Loot Dropped From Enemies!")
    print("=====================================")
    for enemy in enemies:
        print(f'Simming {enemy.name} drop list now!')
        drop_list = enemy.generate_drop_list()
        [print(i) for i in drop_list]


if __name__ == '__main__':
    testing_loot_list = [
        {
            'item_id': 100,
            'item_name': 'Boots Of Running',
            'item_source': 'BBEG',
            'drop_chance': 0.9999
        },
        {
            'item_id': 200,
            'item_name': 'Gloves Of Holding',
            'item_source': 'BBEG',
            'drop_chance': 0.25
        },
        {
            'item_id': 300,
            'item_name': 'Shirt Of Wearing',
            'item_source': 'BBEG',
            'drop_chance': 0.25
        },
        {
            'item_id': 400,
            'item_name': 'Pants Of Covering',
            'item_source': 'BBEG',
            'drop_chance': 0.25
        },
        {
            'item_id': 500,
            'item_name': 'Hat Of Headwarming',
            'item_source': 'BBEG',
            'drop_chance': 0.1
        }
    ]

    drop_list_holder = []
    test_size = 100000
    for _ in range(test_size):
        bbeg_loot = [Loot(i['item_id'], i['item_name'], i['item_source'], i['drop_chance']) for i in testing_loot_list if i['item_source'] == 'BBEG']
        bbeg = Boss(tier_dropper=False, loot_table=bbeg_loot, raid_size=10, name='BBEG')
        drop_list_holder.append(bbeg.generate_drop_list())

    flat_list = []
    for element in drop_list_holder:
        for thing in element:
            flat_list.append(thing.item_id)
    counts = Counter(flat_list)
    print(counts)
    print_list = []
    for k, v in counts.items():
        print_list.append(f'{k=}: {v/(test_size)}')
    print_list.sort()
    print(print_list)
