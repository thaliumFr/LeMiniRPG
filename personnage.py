# To avoid circular imports because of type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from inventory import Inventory

from dataclasses import *
from Systems.pybehaviour import *


@dataclass(init=False)
class personnage (PyBehaviour):
    @dataclass
    class Effects:
        Power: int = 0
        Shield: int = 0
    inventory: Inventory
    health: float
    currentHealth: float
    baseDamage: float
    effects: Effects

    def __init__(self, inventory: Inventory, health: float, baseDamage: float, effects: Effects = Effects()) -> None:
        super().__init__()
        self.inventory, self.health, self.currentHealth, self.baseDamage, self.effects = inventory, health, health, baseDamage, effects
        self.inventory.perso = self

    def damage(self, damages: int):
        from math import exp

        protection = 0
        DecreaseByLvl = 0.4

        inv = self.inventory

        ChestplateImportance = .5
        LeggingImportance = .3
        HelmetImportance = .2

        if inv.chestplate != None:
            protection += inv.chestplate.defense * ChestplateImportance
        if inv.legging != None:
            protection += inv.legging.defense * LeggingImportance
        if inv.helmet != None:
            protection += inv.helmet.defense * HelmetImportance

        protection = round(DecreaseByLvl/exp(protection)-DecreaseByLvl+1, 1)

        self.health -= damages*protection
