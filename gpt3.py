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
   
##################################################
# Second prompt

"""
Solve advent of code 2022 day 2
"""

import os
from shared.readdayinput import readdayinput

def first_half(dayinput):
    """
    Solve first half of day 2
    """
    valid_passwords = 0
    for line in dayinput:
        line = line.split()
        min_max = line[0].split('-')
        min_max = [int(x) for x in min_max]
        letter = line[1][0]
        password = line[2]
        count = password.count(letter)
        if count >= min_max[0] and count <= min_max[1]:
            valid_passwords += 1
    return valid_passwords

def second_half(dayinput):
    """
    Solve second half of day 2
    """
    valid_passwords = 0
    for line in dayinput:
        line = line.split()
        min_max = line[0].split('-')
        min_max = [int(x) for x in min_max]
        letter = line[1][0]
        password = line[2]
        if (password[min_max[0]-1] == letter) ^ (password[min_max[1]-1] == letter):
            valid_passwords += 1
    return valid_passwords

def app():
    """
    runs day application
    """
    dayinput = readdayinput()
    half_one = first_half(dayinput)
    half_two = second_half(dayinput)
    print(half_one, half_two)

if __name__ == "__main__":
    """
    MAIN APP
    """
    app()
