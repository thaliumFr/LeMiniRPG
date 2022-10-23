# To avoid circular imports because of type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from inventory import Inventory

from dataclasses import dataclass
from Systems.pybehaviour import *


@dataclass
class Item (PyBehaviour):
    weight: float
    slotSize: int
    inv: Inventory = None

    def Use(self):
        pass


@dataclass()
class consomable(Item, PyBehaviour):
    HealthBoost: float = 0
    PowerBoost: float = 0
    ShieldBoost: float = 0

    def Use(self):
        from tools.math import clamp
        super().Use()
        self.inv.Remove(self)

        perso = self.inv.perso
        perso.health = clamp(
            perso.currentHealth+(self.HealthBoost/100*perso.health), 0, perso.health)
        perso.effects.Power = clamp(
            perso.effects.Power+self.PowerBoost, 0, 100)
        perso.effects.Shield = clamp(
            perso.effects.Shield+self.ShieldBoost, 0, 100)

    def __str__(self) -> str:
        _repr = f"Consomable"
        if self.HealthBoost > 0:
            _repr += f"\n| Health Boost : {self.HealthBoost}%"
        if self.PowerBoost > 0:
            _repr += f"\n| Power Boost : {self.PowerBoost}%"
        if self.ShieldBoost > 0:
            _repr += f"\n| Shield Boost : {self.ShieldBoost}%"

        return _repr


@dataclass
class waepon(Item, PyBehaviour):
    class WaeponType:
        Sword = 0
        Axe = 1
        Longsword = 2
        Gun = 3

    damages: tuple = (0, 0)
    waeponType: WaeponType = WaeponType.Sword
    level: int = 0

    def Use(self, ennemi):
        super().Use()
        from random import randint
        ennemi.damage(randint(self.damages[0], self.damages[1]))


@dataclass(init=False)
class armor(Item, PyBehaviour):
    level: int
    defense: float

    def __init__(self, weight: float, slotSize: int, level: int, defense: float | int):
        super().__init__(weight, slotSize)
        from tools.math import clamp
        self.level, self.defense = level, clamp(defense, 0, 100)


class Helmet(armor, PyBehaviour):
    pass


class Chestplate(armor, PyBehaviour):
    pass


class Legging(armor, PyBehaviour):
    pass
