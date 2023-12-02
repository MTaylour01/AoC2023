from GetData import AoCHandler
import math
    
def is_game_valid(line, maximums):
    _, minigames = line.split(": ")
    for minigame in minigames.split("; "):
        for col in minigame.split(", "):
            num, colour = col.split(" ")
            if int(num) > maximums[colour]:
                return False
    return True


def part1(data):
    maximums = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    valid_games = [game for game in data.splitlines() if is_game_valid(line=game, maximums=maximums)]
    ids = [int(line.split(":")[0].split(" ")[1]) for line in valid_games]
    return (sum(ids))

def min_cubes(line):
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    _, minigames = line.split(": ")
    for minigame in minigames.split("; "):
        for col in minigame.split(", "):
            num, colour = col.split(" ")
            mins[colour] = max(mins[colour], int(num))
    return mins.values()
    
def part2(data):
    mins = [min_cubes(line) for line in data.splitlines()]
    powers = [math.prod(line) for line in mins]
    return sum(powers)
    
def main():
    handler = AoCHandler(day=2)
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()
    