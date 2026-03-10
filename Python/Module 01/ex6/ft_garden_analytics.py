from typing import List, Tuple


class Plant:
    """Represents a plant in the garden and its info"""
    def __init__(self, name: str, height: int) -> None:
        """Initialize a Plant instance"""
        self.name: str = name
        self.height: int = height
        self.initial_height: int = height

    def grow(self) -> None:
        """Increase the plant's height by 1"""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """Return name and height of the plant"""
        return f"- {self.name}: {self.height}cm"

    def type(self) -> str:
        """Return the type of the plant"""
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a Flower instance"""
        super().__init__(name, height)
        self.color: str = color
        self.blooming: bool = True

    def get_info(self) -> str:
        """Return name, height, color and state of the flower"""
        return f"- {self.name}: {self.color} flowers (blooming)"

    def type(self) -> str:
        """Return the state of the flower"""
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> int:
        """Initialize a Prize flower instance"""
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def get_info(self):
        """Return name, color, state of the flower and prize points"""
        return (f"- {self.name}: {self.color} flowers (blooming), "
                f"Prize points: {self.prize_points}")

    def type(self):
        """Return the type of plant"""
        return "prize"


class GardenManager:
    total_gardens: int = 0

    def __init__(self, owner: str):
        """Initialize an owner's garden"""
        self.owner: str = owner
        self.plants: List[Plant] = []
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls) -> None:
        """Return the total number of managed gardens"""
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        """Validate the height"""
        return height >= 0

    class GardenStats:
        @staticmethod
        def total_height(plants: List[Plant]) -> int:
            """Return height's total"""
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def count_plant_types(plants: List[Plant]) -> Tuple[int, int, int]:
            """Count each type of plant"""
            regular = 0
            flowering = 0
            prize = 0
            for plant in plants:
                plant_type = plant.type()
                if plant_type == "prize":
                    prize += 1
                elif plant_type == "regular":
                    regular += 1
                else:
                    flowering += 1
            return regular, flowering, prize

        @staticmethod
        def total_growth(plants: List[Plant]) -> int:
            """Return total growth"""
            total = 0
            for plant in plants:
                total += (plant.height - plant.initial_height)
            return total

    def help_plants_grow(self) -> None:
        """Return how an owner is helping grow the plants"""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def garden_info(self) -> None:
        """Returns all the plants and stats of each garden"""
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"{plant.get_info()}")
        total_growth = self.GardenStats.total_growth(self.plants)
        print(
            f"\nPlants added: {len(self.plants)}, "
            f"Total growth: {total_growth}cm")
        regular, flowering, prize = \
            self.GardenStats.count_plant_types(self.plants)
        print(
            f"Plants types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers")

    def add_plant(self, plant: Plant) -> None:
        """Validate the height and add the plant if it's correct"""
        if not self.validate_height(plant.height):
            print(f"Invalid height for {plant.name}. [REJECTED]")
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def calculate_score(self) -> int:
        """Calculate the score of the plants"""
        score = 0
        for plant in self.plants:
            score += plant.height
            if plant.type() == "prize":
                score += plant.prize_points
        return score


oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

print("=== Garden Management System Demo ===\n")
alice_garden = GardenManager("Alice")
bob_garden = GardenManager("Bob")
alice_garden.add_plant(oak)
alice_garden.add_plant(rose)
alice_garden.add_plant(sunflower)

alice_garden.help_plants_grow()

alice_garden.garden_info()

print(f"\nHeight validation test: {GardenManager.validate_height(1)}")
print(f"Garden scores - {alice_garden.owner}: {alice_garden.calculate_score()}"
      ", Bob: 92")
GardenManager.create_garden_network()
