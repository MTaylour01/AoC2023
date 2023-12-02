import os

#Create a basic template for days 1-24, skipping if a file for that day already exists
for day in range(1,25):
    if os.path.exists(f'Day{day}.py'):
        continue
    text = f'''from GetData import AoCHandler
    
def part1(data):
    pass
    
def part2(data):
    pass
    
def main():
    handler = AoCHandler(day={day})
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()
    '''
    with open(f'Day{day}.py', 'w') as f:
        f.write(text)