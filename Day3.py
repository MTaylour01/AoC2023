from GetData import AoCHandler
import copy

def outofbounds(x,y,board):
    return x < 0 or y < 0 or x >= len(board) or y >= (len(board[0]))

#Checks if a symbol is diagonal
def is_diag(x,y,board):
    for x2 in range(x-1,x+2):
        for y2 in range(y-1,y+2):
            if outofbounds(x2,y2,board):
                continue
            if board[x2][y2][0].isdigit() and not x==x2:
                continue
            if board[x2][y2][1]:
                return not board[x][y][0] == "."
    return False

def part1(data):
    board = [[[x, not (x.isdigit() or x == ".")] for x in line] for line in data.splitlines()]
    old_board = None
    while board != old_board:
        old_board = copy.deepcopy(board)
        for i,row in enumerate(board):
            for j,board_item in enumerate(row):
                board_item[1] = is_diag(i,j,board)
    #We should now have every part number correctly labelled
    nums = []
    num_acc = ""
    for row in board:
        for board_item in row:
            item, val = board_item
            if val and item.isdigit():
                num_acc = f'{num_acc}{item}'
            elif num_acc:
                nums.append(num_acc)
                num_acc = ""
        if num_acc:
            nums.append(num_acc)
            num_acc = ""
    return sum(int(num) for num in nums)

def get_num(x,y,board, direction="both"):
    if outofbounds(x,y,board):
        return ""
    val = board[x][y][0]
    if not val.isdigit():
        return ""
    if direction != "right":
        left = get_num(x,y-1,board,"left")
    else:
        left = ""
    if direction != "left":
        right = get_num(x,y+1,board,"right")
    else:
        right = ""
    return f'{left}{val}{right}'

def is_valid_gear(x,y,board):
    if board[x][y][0] != "*":
        return False
    posns = []
    for x2 in range(x-1, x+2):
        for y2 in range(y-1,y+2):
            if outofbounds(x2,y2,board):
                continue
            if board[x2][y2][0].isdigit():
                posns.append((x2,y2))
    dupes = []
    for (x2,y2) in posns:
        if (x2,y2+1) in posns:
            dupes.append((x2,y2))
    for posn in dupes:
        posns.remove(posn)
    return [get_num(x,y,board) for (x,y) in posns]


    
def part2(data):
    board = [[[x, False] for x in line] for line in data.splitlines()]
    for i,row in enumerate(board):
        for j,board_item in enumerate(row):
            board_item[1] = is_valid_gear(i,j,board)
    board = [[n[1] for n in row] for row in board]
    nums = [item for row in board for item in row if item]
    #print(nums)
    return sum([int(num[0]) * int(num[1]) for num in nums if len(num) == 2])
            
    
def main():
    handler = AoCHandler(day=3)
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()
    