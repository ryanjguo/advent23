def find_calibration(line):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    split_line = list(line)
    for char in split_line:
        if char in nums:
            first_num = char
            break
    
    for char in reversed(split_line):
        if char in nums:
            last_num = char
            break

    return first_num + last_num

def read_file(filepath):
    sum = 0
    with open(filepath, 'r') as file:
        for line in file:
            calibration = find_calibration(line.strip())
            sum += int(calibration)
    
    return sum

print(read_file('d1.txt'))
