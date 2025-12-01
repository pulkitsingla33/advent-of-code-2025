current_position = 50
zero_counter = 0


def find_new_position(current_position, direction, distance):
    
    """
    Find a new position given the current position, direction, and distance.

    Args:
    current_position (int): The current position.
    direction (str): The direction to move ('L' or 'R').
    distance (int): The distance to move.

    Returns:
    tuple: A tuple containing the new position and the number of zeros crossed.
    """
    zero_crossing = abs(distance // 100)
    distance = distance % 100
    if(direction == 'L'):
        new_pos = current_position - distance
        if(new_pos < 0):
            new_pos = 100 + new_pos
            if(current_position != 0):
                zero_crossing += 1
    else:
        new_pos = current_position + distance
        if(new_pos >= 100):
            new_pos = new_pos - 100
            if(new_pos != 0):
                zero_crossing += 1
    return (new_pos, zero_crossing)



with open('input.txt') as f:
    lines = [line.strip() for line in f]


for line in lines:
    direction, distance = line[0], line[1:]
   
    distance = int(distance)

    current_position, zero_crossing = find_new_position(current_position, direction, distance)
    
    if(current_position == 0):
        zero_counter += 1
    zero_counter += zero_crossing

print("Zeros encountered:", zero_counter)
print("Total Lines Processed:", len(lines))
print("Current Position:", current_position)

    