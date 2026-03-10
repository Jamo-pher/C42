"""Create multiple plants and displays their information"""


class Plant:
    """Represents a plant in the garden and its info"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """Print the plant's info upon creation"""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


print("=== Plant Factory Output ===")
list_plants = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]

plants = []

for data in list_plants:
    plant = Plant(data[0], data[1], data[2])
    plants.append(plant)
    plant.get_info()

print("\nTotal plants created: 5")
