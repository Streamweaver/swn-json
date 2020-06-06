from dataparser import DataParser


class ShipDefense(DataParser):

    def __init__(self, data):
        super(ShipDefense, self).__init__(data)
        self.adjustments = {}
        self._parse_adjustments()

    def _parse_adjustments(self):
        adjustment_list = self.data["adjustments"].split('|')
        for adjustment in adjustment_list:
            item = adjustment.split(':')
            if len(item) > 1:
                self.adjustments[item[0]] = item[1]

    def data_dict(self):
        data = {
            'name': self.data['Ship Defense'],
            'cost': {
                'value': self.cost,
                'scales': self.cost_scale
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
            'adjustments': self.adjustments
        }
        return data
