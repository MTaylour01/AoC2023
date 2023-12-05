from GetData import AoCHandler
import functools
    
class Mapping():

    def __init__(self, domain, range, map):
        self.domain = domain
        self.range = range
        self.map = map

    def __str__(self):
        return f'Domain: {self.domain}, Range: {self.range}, Mappings: {self.map}'
    
    @classmethod
    def from_lines(cls, lines):
        map_domain, map_range = lines[0].split(" ")[0].split("-to-")
        map = []
        for line in lines[1:]:
            start_range, start_domain, range_length = [int(num) for num in line.split(" ")]
            map.append((start_domain, start_range, range_length))
        return cls(map_domain, map_range, map)        

    def get_mapping(self, num, backwards=False):
        for (start_dom, start_ran, range_length) in self.map:
            if not backwards:
                dom = start_dom
                ran = start_ran
            else:
                dom = start_ran
                ran = start_dom
            if num >= dom and num < (dom + range_length):
                new = ran + num - dom
                return new
        return num
    


def part1(data):
    sections = data.split("\n\n")
    seeds = [int(n) for n in sections[0].split(": ")[1].split(" ")]
    maps_lines = [section.splitlines() for section in sections[1:]]
    maps = [Mapping.from_lines(map_lines) for map_lines in maps_lines]
    for map in maps:
        seeds = [map.get_mapping(seed) for seed in seeds]
    return min(seeds)

    
def part2(data):
    sections = data.split("\n\n")
    seeds = []
    for start, length in zip(*[iter(sections[0].split(": ")[1].split(" "))]*2):
        min_num, max_num = (int(start), int(start)+int(length))
        seeds.append((min_num, max_num))
    maps_lines = [section.splitlines() for section in sections[1:]]
    maps = [Mapping.from_lines(map_lines) for map_lines in maps_lines]
    maps.reverse()
    i = 0
    while True:
        num = i
        for map in maps:
            num = map.get_mapping(num, backwards=True)
        for (min_num, max_num) in seeds:
            if num >= min_num and num < max_num:
                return i
        i+=1
    
def main():
    handler = AoCHandler(day=5)
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()
    