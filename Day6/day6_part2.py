def main():
    with open("Day6/input.txt", "r") as file:
        line = file.read().strip()

        lines=line.split("\n")
        grand_total = 0

        for i in range(len(lines)):
            lines[i] = [char for char in lines[i]]

        while len(lines[-1]) != len(lines[0]):
            lines[-1].append(' ')

        

        current_total = 0
        current_symbol = ''

        for i in range(len(lines[0])):
            current_num = ''
            
            for j in range(len(lines)):
                if j == len(lines)-1:
                    if lines[j][i] == '*' or lines[j][i] == '+':
                        current_symbol = lines[j][i]
                        grand_total += current_total
                        current_total = int(current_num)
                    elif current_num != '':
                        if current_symbol == '*':
                            current_total *= int(current_num)
                        elif current_symbol == '+':
                            current_total += int(current_num)
                    # print("Current Total after column", i, "is:", current_total)
                    break
                  
                if lines[j][i].isdigit():
                    current_num += lines[j][i]
            
        grand_total += current_total
        print("Grand Total:", grand_total)
        


if __name__ == "__main__":
    main()