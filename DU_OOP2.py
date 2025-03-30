class Device:
    def __init__(self, brand, power):
        self._brand = brand
        self.power = power

    def turn_on(self):
        return f"{self.brand} device is now ON."

    def turn_off(self):
        return f"{self.brand} device is now OFF."


class Coffee_Machine(Device):
    def __init__(self, brand, power, speed_levels):
        self.speed_levels = speed_levels
        super().__init__(brand, power)

    def Blend(self):
        return f"{self.brand} blender is blending things with {self.speed_levels}speed levels."


class Meat_grinder(Device):
    def __init__(self, brand, power, blade_material):
        self.blade_material = blade_material
        super().__init__(brand, power)

    def Make_coffee(self):
        return f"{self.brand} meat grinder is grinding meat with {self.water_capacity}blades."


