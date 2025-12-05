
def main():
    range_data = []
    values_data = []
    with open("Day5/input.txt", "r") as file:
        file_data = file.read().strip().split("\n")
        range_vals = True
        
        for file_data_val in file_data:
            if file_data_val == "":
                range_vals = False
                continue

            if range_vals:
                range_data.append(file_data_val.split("-"))
            else:
                values_data.append(int(file_data_val))
    
    range_vals_min = [int(r[0]) for r in range_data]
    range_vals_difference = [int(r[1]) - int(r[0]) for r in range_data]

    fresh_count = 0

    for value in values_data:
        for i in range(len(range_vals_min)):
            if range_vals_min[i] <= value <= (range_vals_min[i] + range_vals_difference[i]):
                fresh_count += 1
                break

    print("Fresh Count:", fresh_count)


if __name__ == "__main__":
    main()