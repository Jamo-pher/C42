import sys
from typing import Dict, List

print("=== Inventory System Analysis ===")

if (len(sys.argv) < 2):
    print("No items provided. Usage: python3 ft_inventory_system.py "
          "<item1:qty> <item2:qty> ...")
else:
    inventory: Dict[str, int] = {}
    arg: int
    argv_len: int = len(sys.argv)
    try:
        for arg in sys.argv[1:]:
            parse: List[str] = arg.split(":")
            item: str = parse[0]
            qty: int = int(parse[1])
            if item in inventory:
                inventory[item] += qty
            else:
                inventory[item] = qty
        unique_items: int = len(inventory)
        qty: int
        total_items: int = 0
        for qty in inventory.values():
            total_items += qty
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {unique_items}")

        print("\n=== Current Inventory ===")
        item: str
        count: str = ""
        for item, qty in inventory.items():
            percent = (qty / total_items) * 100
            if qty > 1 or qty == 0:
                count = "units"
            else:
                count = "unit"
            print(f"{item}: {qty} {count} ({percent:.1f}%)")

        print("\n=== Inventory Statistics ===")
        first: int = 0
        first_name: str = ""
        name: str
        current: int
        for name, current in inventory.items():
            if current > first:
                first = current
                first_name = name
        print(f"Most abundant: {first_name} ({first} units)")

        last: int = 1
        last_name: str = ""
        name2: str
        current2: int

        for name2, current2 in inventory.items():
            if current2 <= last:
                last = current2
                last_name = name2
        count: str = ""
        if last > 1 or last == 0:
            count = "units"
        else:
            count = "unit"
        print(f"Least abundant: {last_name} ({last} {count})")

        print("\n=== Item Categories ===")
        abundant: Dict[str, int] = {}
        moderate: Dict[str, int] = {}
        scarce: Dict[str, int] = {}
        for item, qty in inventory.items():
            if qty >= 7:
                abundant[item] = qty
            elif qty >= 4 and qty <= 6:
                moderate[item] = qty
            else:
                scarce[item] = qty
        print(f"Abundant = {abundant}")
        print(f"Moderate = {moderate}")
        print(f"Scarce = {scarce}")

        print("\n=== Item Categories ===")
        restock: List[str] = []
        for item, qty in inventory.items():
            if qty == 1:
                restock.append(item)
        print(f"Restock needed: {restock}")

        print("\n=== Dictionary Properties Demo ===")
        print(f"Dictionary keys: {list(inventory.keys())}")
        print(f"Dictionary values: {list(inventory.values())}")

        sword_exist: bool = inventory.get('sword') is not None
        print(f"Sample lookup - 'sword' in inventory: {sword_exist}")

    except ValueError:
        print("Items format error. Usage: python3 ft_inventory_system.py "
              "<item1:qty> <item2:qty> ...")
