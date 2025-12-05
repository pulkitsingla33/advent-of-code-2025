
def main():
    with open("Day4/input.txt", "r") as file:
        line = file.read().strip()
        rows = line.split("\n")
        row_len = len(rows[0])
        col_len = len(rows)
        
        total_rolls = 0

        while True:
            initial_matrix = [[0 for _ in range(row_len)] for _ in range(col_len)]
            
            
            for i in range(col_len):
                for j in range(row_len):
                    if(rows[i][j] == '@'):
                        for m in range(i - 1, i + 2):
                            for n in range(j - 1, j + 2):
                                if 0 <= m < col_len and 0 <= n < row_len:
                                    if(not(m == i and n == j)):
                                        initial_matrix[m][n] += 1

            # print("Final Matrix:", initial_matrix)

            access_count = 0
            for i in range(col_len):
                for j in range(row_len):
                    if initial_matrix[i][j] < 4 and rows[i][j] == '@':
                        access_count += 1
                        rows[i] = rows[i][:j] + '.' + rows[i][j+1:]

            
            # print("Access Count:", access_count)
            total_rolls += access_count
            if(access_count == 0):
                    break
            # break

        print("Total Rolls:", total_rolls)

if __name__ == "__main__":
    main()