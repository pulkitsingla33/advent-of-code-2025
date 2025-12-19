
def main():
    with open("Day6/input.txt", "r") as file:
        line = file.read().strip()
        
        lines=line.split("\n")

        grand_total = 0

        for i in range(len(lines)):
            if i == len(lines)-1:
                lines[i] = [char for char in lines[i] if not char.isspace()]
                break

            lines[i] = lines[i].split(" ")
            lines[i] = [int(x) for x in lines[i] if x.isdigit()]

        totals = lines[0]
        
        for i in range(len(totals)):
            for j in range(1,len(lines)-1):
                if lines[-1][i] == '*':
                    totals[i] *= lines[j][i]
                elif lines[-1][i] == '+':
                    totals[i] += lines[j][i]

        grand_total = sum(totals)

        print("Grand Total:", grand_total)


if __name__ == "__main__":
    main()