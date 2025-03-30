class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def turn_on(self):
        return f"{self.brand} device is now ON."

    def turn_off(self):
        return f"{self.brand} device is now OFF."


class Coffee_machine(Device):
    def __init__(self, brand, power, water_capacity):
        super().__init__(brand, power)
        self.water_capacity = water_capacity


    def Make_coffee(self):
        return f"{self.brand} coffee machine is making coffee with {self.water_capacity} liters of water."

class Blender(Device):
    def __init__(self, brand, power, speed_levels):
        self.speed_levels = speed_levels
        super().__init__(brand, power)

    def Blend(self):
        return f"{self.brand} blender is blending things with {self.speed_levels} speed levels."


class Meat_grinder(Device):
    def __init__(self, brand, power, blade_material):
        self.blade_material = blade_material
        super().__init__(brand, power)

    def Grind_meat(self):
        return f"{self.brand} meat grinder is grinding meat with {self.blade_material} blades."


if __name__ == "__main__":
    coffee_machine = Coffee_machine("Nespresso", 1500, 1.5)
    blender = Blender("Philips", 800, 5)
    meat_grinder = Meat_grinder("Bosch", 1200, "stainless steel")

    print(coffee_machine.turn_on())
    print(coffee_machine.Make_coffee())
    print(blender.turn_on())
    print(blender.Blend())
    print(meat_grinder.turn_on())
    print(meat_grinder.Grind_meat())


