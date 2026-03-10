def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive(i):
        if i > days:
            print("Harvest time!")
            return
        print(f"Day {i}")
        recursive(i + 1)
    recursive(1)
