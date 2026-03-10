"""Plant hierarchy module with Flower, Tree and Vegetable subclasses."""


class Plant:
    """Represents a plant in the garden and its info."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant instance."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Print a description of the plant."""
        return f"{self.name}: {self.height}cm,{self.age} days"


class Flower(Plant):
    """Represents a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower instance."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Print a message indicating that the flower is blooming"""
        print(f"{self.name} is blooming with beautifully!")

    def get_info(self) -> str:
        """Get the flower's info and return it as a string"""
        return f"{self.name}, {self.height}cm, \
{self.age} days, {self.color} color"


class Tree(Plant):
    """Represents a tree plant."""

    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        """Initialize a Tree instance"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.square_meters: float = ((self.height * self.trunk_diameter) / 10)

    def produce_shade(self) -> None:
        """Print the shade information"""
        print(
            f"{self.name} provides {self.square_meters} meters of shade")

    def get_info(self) -> str:
        """Get the tree's info and return it as a string"""
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, \
{self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Represents a vegetable plant"""

    def __init__(
                self, name: str, height: int, age: int,
                harvest_season: str, nutritional_value: str) -> None:
        """Initialize a Vegetable instance"""
        super().__init__(name, height, age)
        self.nutritional_value: str = nutritional_value
        self.harvest_season: str = harvest_season

    def nutrition(self) -> None:
        """Print nutritional values"""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def get_info(self) -> str:
        """Get the vegetable's info and return it as a string"""
        return f"{self.name} (Vegetable): {self.height}cm, \
{self.age} days, {self.harvest_season} harvest"


print("=== Garden Plant Types ===\n")

rose: Flower = Flower("Rose", 25, 30, "red")
sunflower: Flower = Flower("Sunflower", 30, 35, "yellow")

oak: Tree = Tree("Oak", 500, 1825, 50)
pine: Tree = Tree("Pine", 600, 2000, 45)

tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
spinach: Vegetable = Vegetable("Spinach", 62, 45, "spring", "vitamin A")

print(rose.get_info())
rose.bloom()
print(sunflower.get_info())
sunflower.bloom()
print("\n")

print(oak.get_info())
oak.produce_shade()
print(pine.get_info())
pine.produce_shade()
print("\n")

print(tomato.get_info())
tomato.nutrition()
print(spinach.get_info())
spinach.nutrition()
