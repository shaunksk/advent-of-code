"""
Solve advent of code - 2022 - day 2
"""


def solve_part_one(data):
    """
    Solve part one of the puzzle
    """
    return sum(1 for line in data if is_valid_password(line))


def solve_part_two(data):
    """
    Solve part two of the puzzle
    """
    return sum(1 for line in data if is_valid_password_part_two(line))


def is_valid_password(line):
    """
    Check if a password is valid
    """
    min_max, letter, password = line.split()
    min_max = min_max.split('-')
    min_count = int(min_max[0])
    max_count = int(min_max[1])
    count = password.count(letter)
    return min_count <= count <= max_count


def is_valid_password_part_two(line):
    """
    Check if a password is valid
    """
    min_max, letter, password = line.split()
    min_max = min_max.split('-')
    min_count = int(min_max[0])
    max_count = int(min_max[1])
    count = password.count(letter)
    return (password[min_count - 1] == letter) ^ (password[max_count - 1] == letter)


def main():
    """
    Main function
    """
    data = open('input.txt').read().splitlines()
    print(f'Part one: {solve_part_one(data)}')
    print(f'Part two: {solve_part_two(data)}')


if __name__ == '__main__':
    main()
