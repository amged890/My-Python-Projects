# Mines are represented by a "m"
# normal spots ar represented by a "-"
field = [
    ['-', 'm', '-', '-'],
    ['m', '-', '-', '-'],
    ['-', '-', 'm', 'm'],
    ['-', '-', '-', '-'],
    ['-', 'm', 'm', '-']
]

# [[2, 'm', 1 ,0]]
final_field = []
mine = 0
for row in range(len(field)):
    # print(row)

    for col in range(len(field[row])):

        if field[row][col] == 'm':
            print(f"Position row {row} col {col} is a mine")

        elif field[row][col] == '-':
            print(f"Position row {row} col {col} is not a mine")
