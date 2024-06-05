# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[], play_order={
    
}):
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    last_five = "".join(opponent_history[-5:])
    if len(last_five) == 5:
        if last_five in play_order.keys(): # already saw pattern
            play_order[last_five] += 1
        else: # new pattern found
            play_order[last_five] = 1

    last_four = ''
    for y in opponent_history[-4:]:
        last_four += y
    
    potential_plays = [
        last_four + x for x in ['R','P','S']
    ]

    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }
# 
    if (len(last_five) == 5 and 
    (
        potential_plays[0] in play_order.keys() or
        potential_plays[1] in play_order.keys() or
        potential_plays[2] in play_order.keys()
        )
    ): 
        prediction = max(sub_order, key=sub_order.get)[-1:]
    else:
        prediction = random.choice(['R','P','S'])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    guess = ideal_response[prediction]

    # guess = "R"
    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    return guess