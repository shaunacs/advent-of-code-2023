def list_games(data_input):
    game_data_input = open(data_input)
    games_list = []

    for game in game_data_input:
        games_list.append(game.strip().split(':'))
    
    return games_list



def get_results_list(data_set):
    results_list = []

    for result in data_set:
        results_list.append(result.split(','))
    
    return results_list

def get_max_color_result(data_set):
    red = 0
    green = 0
    blue = 0

    all_cube_colors = []

    for result in data_set:
        set_result = result.split(',')

        for i in set_result:
            all_cube_colors.append(i.strip())
    
    for cube in all_cube_colors:
        if cube.__contains__('red'):
            red_split = cube.split(' ')

            if int(red_split[0]) > red:
                red = int(red_split[0])
        elif cube.__contains__('green'):
            green_split = cube.split(' ')

            if int(green_split[0]) > green:
                green = int(green_split[0])
        elif cube.__contains__('blue'):
            blue_split = cube.split(' ')
            # print(type(int(blue_split[0])))
            # print(type(blue))

            if int(blue_split[0]) > blue:
                blue = int(blue_split[0])

    return {'red': red, 'green': green, 'blue': blue}
        
def solve_part_1(games):
    red_needed = 12
    green_needed = 13
    blue_needed = 14

    possible_sum = 0

    for game in games:

        max_color_results = get_max_color_result(game[1].strip().split(';'))

        if max_color_results['red'] > red_needed:
            continue
        elif max_color_results['green'] > green_needed:
            continue
        elif max_color_results['blue'] > blue_needed:
            continue
        else:
            separate_game = game[0]
            game_number = int(separate_game.split(' ')[-1])
            possible_sum = possible_sum + game_number
    
    return possible_sum


games_list = list_games('./day-2-input.txt')



print(solve_part_1(games_list))