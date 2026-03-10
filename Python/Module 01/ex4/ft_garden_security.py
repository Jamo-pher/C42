"""Garden Security System module to safely manage plant atributes"""


class SecurePlant:
    """Represents a plant with controlled access to height and age"""
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Set the plant's height if valid (non-negative)"""
        if height < 0:
            print(
                "\nInvalid operation attempted: "
                f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Set the plant's age if valid (non-negative)"""
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        """Return the current height of the plant"""
        return self._height

    def get_age(self) -> int:
        """Return the current age of the plant"""
        return self._age

    def get_info(self) -> None:
        """Print the current information of the plant"""
        print(
            f"\nPlant created: {self._name}"
            f"({self._height}cm, {self._age} days)")


print("=== Garden Security System ===")
plant = SecurePlant("Rose", 25, 30)

plant.get_info()
plant.set_age(-10)
plant.set_height(-5)
