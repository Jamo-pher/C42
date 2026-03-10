import math


print("=== Game Coordinate System ===\n")
try:
    position = (10, 20, 6)
    print(f"Position created: {position}")

    origin = (0, 0, 0)

    x1, y1, z1 = origin
    x2, y2, z2 = position

    distance: int = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {origin} and {position}: {round(distance, 2)}")
except ValueError and TypeError:
    print("Incorrect Coordinates")

coord_numbers: str = "3,4,5"
print(f"\nParsing coordinates: {coord_numbers}")

try:
    nums: int = coord_numbers.split(",")
    parsed_position = (int(nums[0]), int(nums[1]), int(nums[2]))
    print(f"Parsed position: {parsed_position}")
    x, y, z = parsed_position
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance between {origin} and {parsed_position}: "
          f"{round(distance, 2)}")
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


except Exception as e:
    print(f"Error parsing coordinates: {e}")

invalid_coord = "abc,def,ghi"
print(f"\nParsing invalid coordinates: {invalid_coord}")
try:
    nums = invalid_coord.split(",")
    parsed_position = (int(nums[0]), int(nums[1]), int(nums[2]))

except Exception as e:
    print(f"Error parsing coordinates: {e}")
    print("Error details - Type:", type(e).__name__ + ",", "Args:", e.args)
