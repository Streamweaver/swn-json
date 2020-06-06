from dataparser import DataParser


class ShipWeapon(DataParser):

    def __init__(self, data):
        self.stack_size = None
        data = self._parse_stack_size(data)
        super(ShipWeapon, self).__init__(data)

    def _parse_stack_size(self, data):
        cost = data["Cost"].split('/')
        if len(cost) > 1:
            self.stack_size = self._parse_stack_value(cost[1])
            data["Cost"] = cost[0]
        return data

    def _parse_stack_value(self, stack):
        multiple = 1
        if stack.endswith('k'):
            multiple = 1000
            stack = stack[:-1]
        if stack.endswith('m'):
            multiple = 1000000
            stack = stack[:-1]
        return round(float(stack) * multiple)

    def data_dict(self):
        data = {
            "name": self.data["Ship Weapon"],
            'cost': {
                'value': self.cost,
                'scales': self.cost_scale,
                'stackSize': self.stack_size
            },
            'power': {
                'cost': self.power,
                'scales': self.power_scale
            },
            'mass': {
                'cost': self.mass,
                'scales': self.mass_scale
            },
            'hullClass': self.data['Class'],
            'dmg': self.data["Dmg"],
            'hardports': int(self.data["Hard"]),
            'techLevel': int(self.data["TL"]),
            'qualities': self.data["Qualities"]
        }
        return data
