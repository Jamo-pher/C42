"""Garden Plant Registry module"""


class Plant:
    """Represents a plant in the garden and its info"""
    def __init__(self, name: str, height: int, longevity: int) -> None:
        """Initialize a Plant instance"""
        self.name: str = name
        self.height: int = height
        self.longevity: int = longevity


print("=== Garden Plant Registry ===")

plant1 = Plant("Rose", 30, 25)
plant2 = Plant("Sunflower", 25, 45)
plant3 = Plant("Cactus", 15, 120)


print(f"{plant1.name}: {plant1.height}cm, {plant1.longevity} days old")
print(f"{plant2.name}: {plant2.height}cm, {plant2.longevity} days old")
print(f"{plant3.name}: {plant3.height}cm, {plant3.longevity} days old")
