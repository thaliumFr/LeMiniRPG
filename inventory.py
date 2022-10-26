from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from personnage import personnage
from dataclasses import dataclass, field
from Systems.pybehaviour import PyBehaviour
from typing import List
import item


@dataclass(repr=False)
class Inventory(PyBehaviour):
    maxWeight: float = 40
    maxItems: int = 15
    helmet: item.Helmet = None  # type: ignore
    chestplate: item.Chestplate = None  # type: ignore
    legging: item.Legging = None  # type: ignore
    content: List = field(default_factory=list)
    perso: personnage = None

    @property
    def weight(self):
        weight = 0
        for obj in self.content:
            weight += obj.weight
        return weight

    @property
    def ItemsSizes(self):
        Size = 0
        for obj in self.content:
            Size += obj.slotSize
        return Size

    def Add(self, obj: item.Item):

        if (self.weight + obj.weight <= self.maxWeight) & (self.ItemsSizes + obj.slotSize <= self.maxItems):
            obj.inv = self
            self.content.append(obj)
        else:
            return Exception("Can't fit that item in the inventory")

    def Remove(self, obj: item.Item):
        self.content.remove(obj)
        obj.inv = None
        return

    def __repr__(self) -> str:
        result = f"Weight: {self.weight}/{self.maxWeight}"
        result += f"\nItems size: {self.ItemsSizes}/{self.maxItems}"

        result += f"\nArmor:"
        result += f"\n      - Helmet: {self.helmet}"
        result += f"\n      - Chestplate: {self.chestplate}"
        result += f"\n      - Legging: {self.legging}"

        result += f"\nContent:"
        if len(self.content) <= 0:
            result += f"\n      EMPTY"
        else:
            for item in self.content:
                result += f"\n      - {item}"

        return result
