from personnage import *
from inventory import *
import item
from Systems.pybehaviour import PyBehaviour


if __name__ == "__main__":

    PyBehaviour.VerifyFolders()

    chestplate = item.Chestplate(
        weight=20,
        slotSize=2,
        level=1,
        defense=15
    )
    legging = item.Legging(
        weight=15,
        slotSize=2,
        level=1,
        defense=10
    )

    supraPopo = item.consomable(
        weight=1,
        slotSize=1,
        HealthBoost=30,
        PowerBoost=10
    )

    Pru = personnage(
        inventory=Inventory(),
        health=40,
        baseDamage=3
    )
    Pru.Save("Pru")

    Pru.Show()
