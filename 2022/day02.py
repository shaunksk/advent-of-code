
import os

f = open(os.path.dirname(os.path.abspath(__file__)) + '/day02.txt', 'r')
content = f.read()
f.close()

content = content.split('\n')
content = [x.split(' ') for x in content]
content = content[:-1]
# content = content[:1]
# print(content)

#########PART 1###########
score=0
for combo in content:
    round_score = 0
    outcome = ''
    if combo[0] == 'A' and combo[1] == 'Y': outcome = 'win'
    elif combo[0] == 'A' and combo[1] == 'Z': outcome = 'lose'
    elif combo[0] == 'B' and combo[1] == 'X': outcome = 'lose'
    elif combo[0] == 'B' and combo[1] == 'Z': outcome = 'win'
    elif combo[0] == 'C' and combo[1] == 'X': outcome = 'win'
    elif combo[0] == 'C' and combo[1] == 'Y': outcome = 'lose'
    else: outcome = 'draw'

    if outcome == 'win': round_score += 6
    elif outcome == 'lose': round_score += 0 
    elif outcome == 'draw': round_score += 3

    if combo[1] == 'X': round_score += 1
    elif combo[1] == 'Y': round_score += 2
    elif combo[1] == 'Z': round_score += 3

    score += round_score

print(score)

#########PART 2###########
score=0
print(content[:5])
combo_dict={
    "A" + 'lose' : 'C',
    "A" + 'win' : 'B',
    "A" + 'draw' : 'A',
    "B" + 'lose' : 'A',
    "B" + 'win' : 'C',
    "B" + 'draw' : 'B',
    "C" + 'lose' : 'B',
    "C" + 'win' : 'A',
    "C" + 'draw' : 'C',
}
for combo in content:
    round_score = 0
    outcome = ''
    if combo[1] == 'X': outcome = 'lose'
    elif combo[1] == 'Y': outcome = 'draw'
    elif combo[1] == 'Z': outcome = 'win'

    if outcome == 'win': round_score += 6
    elif outcome == 'lose': round_score += 0 
    elif outcome == 'draw': round_score += 3

    our_play = combo[0]+outcome
    print(our_play)
    print(combo_dict[our_play])

    if combo_dict[our_play] == 'A': round_score += 1
    elif combo_dict[our_play] == 'B': round_score += 2
    elif combo_dict[our_play] == 'C': round_score += 3

    score += round_score
    # break

print(score)