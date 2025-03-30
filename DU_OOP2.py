class Device:
    def __init__(self, brand, power):
        self._brand = brand
        self.power = power

    def turn_on(self):
        return f"{self.brand} device is now ON."

    def turn_off(self):
        return f"{self.brand} device is now OFF."


class Coffee_Machine(Device):
    def __init__(self, brand, power, water_capacity):
        self.water_capacity = water_capacity
        super().__init__(brand, power)

    def Make_coffee(self):
        return f"{self.brand} coffee machine is making coffee with {self.water_capacity}liters of water."


