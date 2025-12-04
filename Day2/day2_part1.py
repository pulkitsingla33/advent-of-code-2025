#Assumptions Used:
#1. The number of digits in the max and min of the range differ by atmost one digit.

def find_number_of_digits(max, min):
    """
    Find the number of digits in the range from min to max (inclusive).

    Args:
    max (int): The maximum number in the range.
    min (int): The minimum number in the range.

    Returns:
    int: The number of digits in the range.
    """
    count = 0
    starting_num = min
    num_digits_start = len(str(min))

    ending_num = max
    num_digits_end = len(str(max))

    if((num_digits_start % 2) != 0):
        starting_num = pow(10, num_digits_start)
        num_digits_start += 1

    if((num_digits_end % 2) != 0):
        ending_num = pow(10, num_digits_end - 1) - 1
        num_digits_end -= 1

    return (starting_num, ending_num, num_digits_start, num_digits_end)
    

def main():

    ranges = []
    with open('input.txt') as f:
        text = f.read().strip()

        for tokens in text.split(','):
            a, b = tokens.split('-')
            ranges.append((int(a), int(b)))

        # print("Ranges to process:", ranges)

        invalid_nums_sum = 0

        for range_pair in ranges:
            min_range, max_range = range_pair
            (starting_num, ending_num, num_digits_start, num_digits_end) = find_number_of_digits(max_range, min_range)
            starting_num_in_str = str(starting_num)
            ending_num_in_str = str(ending_num)

            range_invalid_nums_sum = 0

            mid_start = num_digits_start // 2
            mid_end = num_digits_end // 2

            starting_first_half = int(starting_num_in_str[:mid_start])
            starting_second_half = int(starting_num_in_str[mid_start:])
            ending_first_half = int(ending_num_in_str[:mid_end])
            ending_second_half = int(ending_num_in_str[mid_end:])
            print("Processing range:", range_pair)
            print("First half range:", starting_first_half, "to", ending_first_half)
            print("Second half range:", starting_second_half, "to", ending_second_half)

            for i in range (starting_first_half, ending_first_half + 1):
                print("Value of i:", i)
                if ((i == starting_first_half) and (starting_second_half > starting_first_half)):
                    continue
                elif((i == ending_first_half) and (ending_second_half < ending_first_half)):
                    continue
                else:
                    range_invalid_nums_sum += int(str(i) * 2)

                print("Current sum of invalid numbers in this range:", range_invalid_nums_sum)

            invalid_nums_sum += range_invalid_nums_sum

        print("Sum of invalid numbers in the given ranges:", invalid_nums_sum)

            
        



if __name__ == "__main__":
    main()
    