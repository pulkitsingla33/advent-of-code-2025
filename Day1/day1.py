current_position = 50
zero_counter = 0


def find_new_position(current_position, direction, distance):
    distance = distance % 100
    if(direction == 'L'):
        new_pos = current_position - distance
        if(new_pos < 0):
            new_pos = 100 + new_pos
    else:
        new_pos = current_position + distance
        if(new_pos >= 100):
            new_pos = new_pos - 100
    return new_pos

with open('input.txt') as f:
    lines = [line.strip() for line in f]
    # print(lines)



for line in lines:
    direction, distance = line[0], line[1:]
    print("Current Position:", current_position)
    current_position = find_new_position(current_position, direction, int(distance))
    
    if(current_position == 0):
        zero_counter += 1

print("Zeros encountered:", zero_counter)
print("Total Lines Processed:", len(lines))
print("Current Position:", current_position)

    