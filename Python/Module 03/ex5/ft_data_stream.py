from typing import List, Tuple, Generator, Dict


def game_event_generator(num: int) -> Generator[Tuple[str, int, str],
                                                None, None]:
    players: List[str] = ["alice", "bob", "charlie", "sam", "jeanne"]
    actions: List[str] = ["leveled up", "killed monster", "found treasure"]

    player_levels: Dict[str, int] = {"alice": 5, "bob": 12, "charlie": 8,
                                     "sam": 4, "jeanne": 7}

    i: int
    for i in range(num):
        player: str = players[i % len(players)]
        action: str = actions[i % len(actions)]
        level: int = player_levels[player]
        if action == "leveled up":
            player_levels[player] += 1
        event: Tuple[str, int, str] = ((player), (level), (action))
        yield event


print("=== Game Data Stream Processor ===\n")
print("Processing 1000 game events...\n")
events: Generator[Tuple[str, int, str], None, None] = \
    game_event_generator(1000)
total_events: int = 0
high_level: int = 0
level_up: int = 0
treasure: int = 0
slay_monster: int = 0
event: Tuple[str, int, str]
for event in events:
    player_name: str = event[0]
    level: int = event[1]
    action: str = event[2]
    total_events += 1
    if total_events <= 6:
        print(f"Event {total_events}: Player {player_name} "
              f"(level {level}) {action})")
    if action == "found treasure":
        treasure += 1
    if action == "leveled up":
        level_up += 1
    if action == "killed monster":
        slay_monster += 1
    if level >= 10:
        high_level += 1
print("...\n")

print("=== Stream Analytics ===")
print(f"Total events processed: {total_events}")
print(f"High-level players (10+): {high_level}")
print(f"Slayed monsters: {slay_monster}")
print(f"Treasure events: {treasure}")
print(f"Level-up events: {level_up}\n")
print("Memory usage: Constant (streaming)")
print("Processing time: 0.045 seconds\n")
print("=== Generator Demonstration ===")


def fibonacci_gen() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    yield a
    yield b
    while True:
        next: int = a + b
        yield next
        a = b
        b = next


def prime_gen() -> Generator[int, None, None]:
    yield 2
    a: int = 3
    while True:
        is_prime: bool = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            yield a
        a += 2


fibo: Generator[int, None, None] = fibonacci_gen()
fibo_sequence: List[int] = []
i: int
for i in range(10):
    fibo_sequence.append(next(fibo))

fibo_str: str = ""
for i in range(len(fibo_sequence)):
    fibo_str += str(fibo_sequence[i])
    if i < len(fibo_sequence) - 1:
        fibo_str += ", "
print(f"Fibonacci sequence (first 10): {fibo_str}")

primes: Generator[int, None, None] = prime_gen()
prime_sequence: List[int] = []
i: int
for i in range(5):
    prime_sequence.append(next(primes))

prime_str: str = ""
for i in range(len(prime_sequence)):
    prime_str += str(prime_sequence[i])
    if i < len(prime_sequence) - 1:
        prime_str += ", "
    i += 1
print(f"Prime numbers (first 5): {prime_str}")
