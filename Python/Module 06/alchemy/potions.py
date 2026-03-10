from .elements import create_fire, create_water, create_earth, create_air


def healing_potion() -> str:
    return (f"Healing potion brewed with {create_fire()} and {create_water()}")


def strenght_potion() -> str:
    return (f"Strenght potion brewed with {create_earth()} "
            f"and {create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {create_air()} "
            f"and {create_water()}")


def wisdom_potion() -> str:
    return ("Wisdom potion brewed with all elements: "
            f"{create_water()}, {create_earth()}, "
            f"{create_fire()}, {create_air()}")
