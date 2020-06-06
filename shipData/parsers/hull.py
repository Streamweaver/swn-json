from dataparser import DataParser

class ShipHull(DataParser):

    def __init__(self, data):
        super(ShipHull, self).__init__(data)
        self.min_crew = 0
        self.max_crew = 0
        self.parse_crew()

    def parse_crew(self):
        crew = self.data['Crew'].split('/')
        self.min_crew = crew[0]
        self.max_crew = crew[1]

    def data_dict(self):
        data = {
            'type': self.data['Hull Type'],
            'cost': self.cost,
            'armor': int(self.data['Armor']),
            'hp': int(self.data['HP']),
            'crew': {
                'min': int(self.min_crew.replace(',', '')),
                'max': int(self.max_crew.replace(',', ''))
            },
            'ac': int(self.data['AC']),
            'power': int(self.data['Power']),
            'mass': int(self.data['Mass']),
            'hardports': int(self.data['Hard']),
            'hullClass': self.data['Class']
        }
        try:
            data['speed'] = int(self.data['Speed'])
        except ValueError:
            data["speed"] = None
        return data

