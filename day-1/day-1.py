def find_first_digit(line_text):
    for char in line_text:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return char
        else:
            continue

def find_last_digit(line_text):
    for char in line_text[::-1]:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return char
        else:
            continue

def list_text_inputs(data_file):
    data_input = open(data_file)
    scrambled_values = []

    for line in data_input:
        scrambled_values.append(line.strip())

    return scrambled_values


def find_calibration_value(scrambled_value):
    first_digit = find_first_digit(scrambled_value)
    last_digit = find_last_digit(scrambled_value)
    calibration_value = int(first_digit + last_digit)

    return calibration_value


calibration_values = []

for line in list_text_inputs('./day-1-input.txt'):
    calibration_values.append(find_calibration_value(line))

print(sum(calibration_values))