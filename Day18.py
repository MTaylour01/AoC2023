from GetData import AoCHandler
    
def part1(data):
    pass
    
def part2(data):
    pass
    
def main():
    handler = AoCHandler(day=18)
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()
    