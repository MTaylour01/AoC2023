from GetData import AoCHandler
import re

def part1(data):
    number_reg = r"\d"
    all_nums = [re.findall(number_reg, line) for line in data.splitlines()]

    all_fsts_lasts = [(line[0], line[-1]) for line in all_nums]
    
    return sum([int(f'{fst}{lst}') for (fst,lst) in all_fsts_lasts])

def part2(data):
    number_reg = r"(?=((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)))"
    all_nums = [re.findall(number_reg, line) for line in data.splitlines()]

    def written_to_digit(num):
        if num.isdigit():
            return num
        num_vals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return str(num_vals.index(num) + 1)

    all_fsts_lasts = [(written_to_digit(line[0][0]), written_to_digit(line[-1][0])) for line in all_nums]

    return sum([int(f'{fst}{lst}') for (fst,lst) in all_fsts_lasts])

def main():
    handler = AoCHandler(day=1)
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()



