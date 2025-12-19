def main():
    with open("Day7/input.txt", "r") as file:
        lines = file.read().split("\n")
        split_counter = 0
        starting = True
        prev_beam_positions = []
        splitting = False

        for line in lines:
            current_beam_positions = []
            splitting = False
            for j in range(len(lines[0])):
                if starting:
                    if line[j] == 'S':
                        current_beam_positions.append(j)
                        # print(f"Starting beam at position: {j}")
                        starting = False
                        splitting = True
                else:
                    if line[j] == '^' and j in prev_beam_positions:
                        if j-1 not in current_beam_positions:
                            current_beam_positions.append(j-1)
                        if j+1 not in current_beam_positions:
                            current_beam_positions.append(j+1)
                        current_beam_positions.remove(j)
                        split_counter += 1
                        splitting = True
                

                if not splitting:
                    current_beam_positions = prev_beam_positions.copy()
            
            print("Current Beam Positions:", current_beam_positions)
            print("Current Split Counter:", split_counter)
            prev_beam_positions = current_beam_positions

        print(f"Number of splits: {split_counter}")
if __name__ == "__main__":
    main()