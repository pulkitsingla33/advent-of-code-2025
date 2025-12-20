def main():
    with open("Day7/input.txt", "r") as file:
        lines = file.read().split("\n")
        starting = True

        beam_counter = [0] * len(lines[0])
        
        for line in lines:
            if starting:
                for j in range(len(line)):
                    if line[j] == 'S':
                        beam_counter[j] += 1
                        starting = False
            else:
                for j in range(len(line)):
                    if line[j] == '^' and beam_counter[j] >0:
                        beam_counter[j-1] += beam_counter[j]
                        beam_counter[j+1] += beam_counter[j]
                        beam_counter[j] = 0

        total_count = sum(beam_counter)
        print(f"Total number of beams at the end: {total_count}")

if __name__ == "__main__":
    main()