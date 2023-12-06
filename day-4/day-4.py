def list_cards(data_input):
    card_data_input = open(data_input)
    card_list = []
    card_list_split = []

    for card in card_data_input:
        card_list.append(card.strip().split(':')[-1])
    
    for card in card_list:
        card_list_split.append(card.split('|'))
    
    return card_list_split

cards = list_cards('./day-4-input.txt')

total_scratchcard_count = 0


for card in cards:
    winner_count = 0
    points_count = 1

    winning_numbers = card[0].strip().split(' ')
    your_numbers = card[1].strip().split(' ')

    while '' in your_numbers:
        your_numbers.remove('')
    
    for num in your_numbers:
        if num in winning_numbers:
            winner_count = winner_count + 1

    while winner_count > 1:
        points_count = points_count * 2
        winner_count = winner_count - 1

    if winner_count >= 1:
        total_scratchcard_count = total_scratchcard_count + points_count


print(total_scratchcard_count)
