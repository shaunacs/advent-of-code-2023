def list_races(data_input):
    race_input_data = open(data_input)
    race_data = []
    

    for line in race_input_data:
        race_data.append(line.strip())
    
    max_race_times = race_data[0].split(':')[-1].strip().split(' ')

    while '' in max_race_times:
        max_race_times.remove('')

    distance_records = race_data[1].split(':')[-1].strip().split(' ')

    while '' in distance_records:
        distance_records.remove('') 

    return {'max race times': max_race_times, 'distance records': distance_records}


def calculate_distance(button_hold_time, race_time):
    return (race_time - button_hold_time) * button_hold_time 

max_race_times = list_races('./day-6-input.txt')['max race times']
distance_records = list_races('./day-6-input.txt')['distance records']

possible_wins_list = []
for i, race in enumerate(max_race_times):

    race_time = int(race)
    button_hold_time = int(race)
    distance_record = int(distance_records[i])
    possibile_wins = 0

    while button_hold_time >= 0:
        distance = calculate_distance(button_hold_time, race_time)

        if distance > distance_record:
            possibile_wins = possibile_wins + 1

        button_hold_time = button_hold_time - 1

    possible_wins_list.append(possibile_wins)

margin_of_error = 0

for i, wins in enumerate(possible_wins_list):
    if i == 0:
        margin_of_error = possible_wins_list[i]
    else:
        margin_of_error = margin_of_error * possible_wins_list[i]

print(margin_of_error)

