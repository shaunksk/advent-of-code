# Part 1 - Dirac Dice

"""
Given starting postion of 2 players 
Player 1 starting position: 7
Player 2 starting position: 10
"""

first_pos, second_pos = 7, 10
first_score, second_score = 0, 0
die_roll = 1

while True:

    first_pos=(first_pos + die_roll*3 + 3 - 1)%10 + 1
    first_score += first_pos
    die_roll += 3
    if first_score >= 1000: break

    second_pos=(second_pos + die_roll*3 + 3 - 1)%10 + 1
    second_score += second_pos
    die_roll += 3
    if second_score >= 1000: break

print("die roll:",die_roll, ", first score:", first_score, ", second score:",second_score)

print("Part 1 Answer:",min(first_score,second_score)*(die_roll-1))

# Part 2 - 