import json
from csv import DictReader

from hull import ShipHull
from fitting import Fitting
from defenses import ShipDefense
from weapons import ShipWeapon


class Collection:

    def __init__(self, input_file, item_class, collection, name):
        self.input_file = input_file
        self.item_class = item_class
        self.data = {
            "type": collection,
            "items": [],
            "properties": {
                "name": name,
            }
        }
        self.parse_data()

    def add_item(self, data):
        self.data["items"].append(data)

    def parse_data(self):
        with open(self.input_file, newline='') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                item = self.item_class(row)
                self.add_item(item.data_dict())


if __name__ == "__main__":
    collections = [
        Collection('../csv/hulls.csv', ShipHull, 'hullTypes', 'Starship Hulls'),
        Collection('../csv/fittings.csv', Fitting, 'fittings', 'Starship Fittings'),
        Collection('../csv/defenses.csv', ShipDefense, 'defenses', 'Starship Defenses'),
        Collection('../csv/weapons.csv', ShipWeapon, 'weapons', "Starship Weapons")
    ]

    data = []
    for collection in collections:
        data.append(collection.data)

    with open('../starship_data.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4, sort_keys=True)
