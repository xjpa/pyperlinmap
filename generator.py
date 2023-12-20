import random
from termcolor import colored, cprint
# https://pypi.org/project/termcolor/
# https://pypi.org/project/noise/
from noise import pnoise2


def generator(cols=10, rows=10):
    data = ["🌳", "🌲", "🌊", "🐟", "🦞", "💦", "🦞", "🐟", "🌊", "🌲", "🌳"]
    seeding = random.randint(0, 100)
    land = ""
    print(f"generating a map of {cols} by {rows}")

    for row in range(rows):
        for col in range(cols):
            noise = pnoise2(row/rows, col/cols, base=seeding)
            noise *= 10  # noise level
            noise = round(noise)
            noise = noise % len(data)

            land += data[noise]
        land += "\n"

    return land


def get_input(question):
    tries = 3
    while tries > 0:
        input = input(colored(question, "blue"))
        if input.isnumeric():
            return int(input)
        else:
            print(colored(
                f"ERROR: not a valid input. INPUT SHOULD BE A NUMBER, try again, you have {tries-1} tries left", "red", "on_white"))
            tries -= 1
    quit()


if __name__ == "__main__":
    columns = get_input("enter the number of columns: ")
    rows = get_input("enter the number of rows: ")
    generated_output = generator(columns, rows)
    print(generated_output)