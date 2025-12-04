
def get_len_factors(start_len, end_len):
    start_factors = [1]
    end_factors = [1]

    for i in range(2, end_len//2 + 1):
        if start_len % i == 0:
            start_factors.append(i)
        if end_len % i == 0:
            end_factors.append(i)
    
    return start_factors, end_factors

def partition_digits_by_size(size, start, end):
    #If start is not a string
    if(type(start) != str):
        start = str(start)
    if(type(end) != str):
        end = str(end)

    start_val = int(start[:size])
    end_val = int(end[:size])

    return start_val, end_val

def number_added(num, added_numbers):
    for n in added_numbers:
        if n == num:
            return True
    return False

def main():

    ranges = []
    with open('Day2/input.txt') as f:
        text = f.read().strip()

        for tokens in text.split(','):
            a, b = tokens.split('-')
            ranges.append((int(a), int(b)))

    total_sum = 0

    for range_val in ranges:
        start, end = range_val
        start_len = len(str(start))
        end_len = len(str(end))
        
        start_len_factors = []
        end_len_factors = []
        range_invalid_sum = 0
        added_numbers = []

        start_len_factors, end_len_factors = get_len_factors(start_len, end_len)
        print("Start len factors:", start_len_factors)
        print("End len factors:", end_len_factors)
        
        if(start_len == end_len):
            for i in start_len_factors:
                start_val, end_val = partition_digits_by_size(i, start, end)
                
                for j in range(start_val, end_val + 1):
                    current_num_str = str(j) * (start_len // i)
                    current_num_int = int(current_num_str)

                    if(j == start_val and current_num_int < start):
                        continue
                    elif(j == end_val and current_num_int > end):
                        continue
                    else:
                        if(not number_added(current_num_int, added_numbers)):
                            range_invalid_sum += current_num_int
                            added_numbers.append(current_num_int)
                            print("Added number:", current_num_int)

        else:
            for i in start_len_factors:
                if start_len == 1:
                    break
                start_val, end_val = partition_digits_by_size(i, start, '9' * start_len)
                
                for j in range(start_val, end_val + 1):
                    current_num_str = str(j) * (start_len // i)
                    current_num_int = int(current_num_str)

                    if(j == start_val and current_num_int < start):
                        continue
                    else:
                        if(not number_added(current_num_int, added_numbers)):
                            range_invalid_sum += current_num_int
                            added_numbers.append(current_num_int)
                            print("Added number:", current_num_int)

            for i in end_len_factors:
                if end_len == 1:
                    break
                start_val, end_val = partition_digits_by_size(i, '1' + '0' * (end_len - 1), end)
                
                
                for j in range(start_val, end_val + 1):
                    current_num_str = str(j) * (end_len // i)
                    current_num_int = int(current_num_str)

                    if(j == end_val and current_num_int > end):
                        continue
                    else:
                        if(not number_added(current_num_int, added_numbers)):
                            range_invalid_sum += current_num_int
                            added_numbers.append(current_num_int)
                            print("Added number:", current_num_int)

        print("Sum of invalid numbers in range", start, "-", end, "is:", range_invalid_sum)
        total_sum += range_invalid_sum
        print(f"Total sum so far is: {total_sum}\n")

    print("Total sum of invalid numbers across all ranges is:", total_sum)

                    
if __name__ == "__main__":
    main()
    