# Mostafa Tarek Amer        Final: Create a Sudoku Class                CMPSC 132


def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(x) for x in row))
    print()

def is_valid_group(group):
    nums = set(range(1, 10))
    for num in group:
        if num in nums:
            nums.remove(num)
        elif num != 0:
            return False, f"Invalid: Contains duplicate {num}"
    return True, "Valid" if not nums else f"Incomplete: Missing {', '.join(map(str, nums))}"

def check_rows(puzzle):
    print("Rows:")
    for i, row in enumerate(puzzle):
        valid, reason = is_valid_group(row)
        print(f"Row {i + 1}: {reason}")
    print()

def check_columns(puzzle):
    print("Columns:")
    for i in range(9):
        column = [row[i] for row in puzzle]
        valid, reason = is_valid_group(column)
        print(f"Column {i + 1}: {reason}")
    print()

def check_sections(puzzle):
    print("Sections:")
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            section = [puzzle[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            valid, reason = is_valid_group(section)
            print(f"Section ({i//3 + 1}, {j//3 + 1}): {reason}")
    print()

def main():
    puzzle = [
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

    print_puzzle(puzzle)
    check_rows(puzzle)
    check_columns(puzzle)
    check_sections(puzzle)

if __name__ == "__main__":
    main()
