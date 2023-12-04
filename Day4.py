from GetData import AoCHandler
import re
    
def intersection(list1, list2):
    return [item for item in list1 if item in list2]

def get_card_score(card):
    card = re.sub(r"\s+", " ", card)
    _, card_vals = card.split(": ")
    winners, guesses = card_vals.split(" | ")
    winning_guesses = intersection(guesses.split(" "), winners.split(" "))
    if winning_guesses:
        return 2**(len(winning_guesses)-1)
    return 0

def part1(data):
    card_scores = [get_card_score(line) for line in data.splitlines()]
    return sum(card_scores)

def get_cards(card):
    card = re.sub(r"\s+", " ", card)
    card_num, card_vals = card.split(": ")
    winners, guesses = card_vals.split(" | ")
    winning_guesses = intersection(guesses.split(" "), winners.split(" "))
    num = int(card_num.split(" ")[1])
    return range(num+1,num+1+len(winning_guesses))
    
def part2(data):
    cards = [line for line in data.splitlines()]
    num_cards_viewed = 0
    cards_to_view = {card: 1 for card in cards}
    lookup = {card: get_cards(card) for card in cards}
    for (curr_card, num) in cards_to_view.items():
        num_cards_viewed+=num
        new_cards = list(lookup[curr_card]) * num
        for new_card in new_cards:
            cards_to_view[cards[new_card-1]] += 1 
    return num_cards_viewed
    
def main():
    handler = AoCHandler(day=4)
    data = handler.get_data()

    handler.submit(part1(data), 1)
    handler.submit(part2(data), 2)

if __name__ == '__main__':
    main()
    