NUM_OF_DIGITS = 12

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

        joltage_sum = 0

        for current_joltage in joltage_vals:
            current_joltage_str = str(current_joltage)
            

            current_joltage_max_pos = 0
            current_joltage_max_digit = 0
            
            current_joltage_value = ''

            for i in range(NUM_OF_DIGITS):
                current_joltage_len = len(current_joltage_str)
                joltage_str_to_test = current_joltage_str[0: current_joltage_len - (NUM_OF_DIGITS - i - 1)]
                current_joltage_max_digit, current_joltage_max_pos = get_max_digit_and_pos(int(joltage_str_to_test))
                current_joltage_value += str(current_joltage_max_digit)
                current_joltage_str = current_joltage_str[current_joltage_max_pos + 1:]


            joltage_sum += int(current_joltage_value)

        print(joltage_sum)

if __name__ == "__main__":
    main()