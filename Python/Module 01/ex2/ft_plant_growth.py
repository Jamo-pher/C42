"""Simulate the growth of a single plant over a period of one week"""


class Plant:
    """Represents a plant in the garden and its info"""
    def __init__(self, name, height, age) -> None:
        """Initialize a Plant instance"""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self) -> None:
        """Increase the plant's height by 1"""
        self.height += 1

    def longevity(self) -> None:
        """Increase the plant's age by 1"""
        self.age += 1

    def get_info(self) -> None:
        """Print the plant's current information"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
i = 1
week = 7
print("=== Day 1 ===")
rose.get_info()
start_height = rose.height
while i < week:
    rose.grow()
    rose.longevity()
    i += 1
print(f"=== Day {week} ===")
rose.get_info()
grow = rose.height - start_height
print(f"Growth this week: +{grow}cm")
