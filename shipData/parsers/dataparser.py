from abc import ABC, abstractmethod


class DataParser(ABC):

    def __init__(self, data):
        self.data = data
        self.cost = 0
        self.cost_scale = False
        self.power = 0
        self.power_scale = False
        self.mass = 0
        self.mass_scale = False

        self._parse_cost_scale()
        self._parse_cost_value()
        self._parse_power()
        self._parse_mass()

    def _parse_cost_value(self):
        data = self.data['Cost'].strip()
        if data == 'No cost' or data == 'Special':
            return
        multiple = 1
        if data.endswith('k'):
            multiple = 1000
            data = data[:-1]
        if data.endswith('m'):
            multiple = 1000000
            data = data[:-1]
        self.cost = round(float(data) * multiple)

    def _parse_cost_scale(self):
        data = self.data['Cost'].strip()
        if data.endswith('*'):
            self.data['Cost'] = data[:-1]
            self.cost_scale = True

    def _parse_power(self):
        if self.data['Power'].endswith('#'):
            self.data['Power'] = self.data['Power'][:-1]
            self.power_scale = True
        self.power = int(self.data['Power'])

    def _parse_mass(self):
        if self.data['Mass'].endswith('#'):
            self.data['Mass'] = self.data["Mass"][:-1]
            self.mass_scale = True
        self.mass = float(self.data["Mass"])

    @abstractmethod
    def data_dict(self):
        pass

