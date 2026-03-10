import sys

print("=== Command Quest ===")
program: str = sys.argv[0]
number: int = len(sys.argv) - 1
if (len(sys.argv) < 2):
    print("No arguments provided!")
    print(f"Program name = {program}")
    print("Total arguments: 1")
else:
    print(f"Program name = {program}")
    print(f"Arguments recieved: {number}")
    i: int = 1
    arg: str
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i += 1
    print(f"Total arguments: {i}")
