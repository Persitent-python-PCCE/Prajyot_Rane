import random


class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def take_damage(self, amount):
        dmg = max(1, amount - self.defense)
        self.health = max(0, self.health - dmg)
        return dmg

    def attack(self, target):
        raw_damage = self.attack_power
        damge_taken = target.take_damage(raw_damage)
        print(f"{self.name} attacks {target.name} Deals Damage: {damge_taken}")

    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 130, 22, 12, 6)  # reuse the parent's setup
        self.rage = 0

    def attack(self, target):
        raw_damage = self.attack_power
        if self.health < self.max_health * 0.30:
            raw_damage *= 2
            print("Berserk Mode!!!! 2x Damage")
        elif self.rage == 5:
            rage_input = int(input("Rage Bar Full deal bonus damage? y or n:"))
            if rage_input == "y":
                raw_damage += 10
            else:
                pass
        else:
            damge_taken = target.take_damage(raw_damage)
            print(f"{self.name} attacks {target.name} Deals Damage: {damge_taken}")
            self.rage += 1


class Mage(Character):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 90, 30, 5, 8)  # reuse the parent's setup
        self.mana = 100

    def attack(self, target):
        raw_damage = self.attack_power
        mana_cost = 30
        if self.mana >= mana_cost:
            raw_damage = int(raw_damage * 1.5)
            damge_taken = target.take_damage(raw_damage)
            print(f"{self.name} attacks {target.name} Deals Damage: {damge_taken}")
            self.health -= 5
        else:
            damge_taken = target.take_damage(raw_damage)
            print(f"{self.name} attacks {target.name} Deals Damage: {damge_taken}")


class Archer(Character):
    def __init__(self, name):
        self.name = name
        super().__init__(name, 100, 24, 7, 12)  # reuse the parent's setup
        self.critical_chance = 0.30

    def attack(self, target):
        raw_damage = self.attack_power
        if random.random() >= self.critical_chance:
            raw_damage *= 2
            damge_taken = target.take_damage(raw_damage)
            print(
                f"{self.name} attacks {target.name} Deals Damage(2x Damage Critical Hit): {damge_taken}"
            )
        else:
            damge_taken = target.take_damage(raw_damage)
            print(f"{self.name} attacks {target.name} Deals Damage: {damge_taken}")


warrior = Warrior("Thor")
mage = Mage("Gandalf")
archer = Archer("Alex")
fighters = [warrior, mage, archer]
while sum(f.is_alive() for f in fighters) > 1:
    fighters.sort(key=lambda fighter: fighter.speed, reverse=True)

    for fighter in fighters:
        if not fighter.is_alive():
            continue
        targets = [f for f in fighters if f != fighter and f.is_alive()]
        if not targets:
            break
        target = targets[0]
        fighter.attack(target)

winner = [f for f in fighters if f.is_alive()][0]
print(f"\n🏆 {winner.name} wins!")
print("Health Status")
for f in fighters:
    print(f"{f.name} :{f.health}  ")
