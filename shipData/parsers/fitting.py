from dataparser import DataParser


class Fitting(DataParser):

    def data_dict(self):
        data = {
            'name': self.data['Ship Fitting'],
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
            'effect': self.data['Effect'],
            'adjustments': {}
        }
        return data
