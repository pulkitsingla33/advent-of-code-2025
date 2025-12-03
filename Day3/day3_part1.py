def get_max_digit_and_pos(number):
    max_digit = 0
    max_digit_pos = 0
    for i in range(len(str(number))):
        if(int(str(number)[i]) > max_digit):
            max_digit = int(str(number)[i])
            max_digit_pos = i

    return max_digit, max_digit_pos

def main():
    with open('input.txt') as f:
        text = f.read().strip()
        joltage_vals = [int(x) for x in text.split('\n')]
        # print(joltage_vals)
        joltage_sum = 0

        for current_joltage in joltage_vals:
            next_joltage_digit = 0
            # current_joltage_reversed_str = str(current_joltage)[::-1]
            current_joltage_str = str(current_joltage)
            current_joltage_max_digit, current_joltage_max_pos = get_max_digit_and_pos(int(current_joltage_str[:len(current_joltage_str)-1]))

            next_joltage_str = current_joltage_str[current_joltage_max_pos + 1:]    
            next_joltage_max_digit, _ = get_max_digit_and_pos(int(next_joltage_str))

            joltage_value = int(str(current_joltage_max_digit) + str(next_joltage_max_digit))
            joltage_sum += joltage_value

        print(joltage_sum)


if __name__ == "__main__":
    main()