class Weapon():

    def __init__(self,bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1

            result =  "shooting..."
        else:
            result =  "no bullets left"
        return result
    def __repr__(self):
        result = f"Remaining bullets: {self.bullets}"
        return  result

# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
