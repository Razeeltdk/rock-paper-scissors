import random

def player(prev_play, opponent_history=[]):
    # look if it's the first game
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default move 
    move = random.choice(["R", "P", "S"])

    # Strategy for Queency
    if len(opponent_history) >= 1:
        if opponent_history[-1] == "R":
            move = "P"  # Paper beats Rock
        elif opponent_history[-1] == "P":
            move = "S"  # Scissors beats Paper
        elif opponent_history[-1] == "S":
            move = "R"  # Rock beats Scissors

    # Strategy for mark
    # predicts based on player's last two moves
    if len(opponent_history) >= 2:
        last_two = "".join(opponent_history[-2:])
        if last_two == "RR":
            move = "P"
        elif last_two == "PP":
            move = "S"
        elif last_two == "SS":
            move = "R"
        elif last_two == "RP":
            move = "S"
        elif last_two == "PS":
            move = "R"
        elif last_two == "SR":
            move = "P"

    # Strategy for don
    # plays the move that would have beaten the player's last move
    if len(opponent_history) >= 1:
        if opponent_history[-1] == "R":
            move = "P"
        elif opponent_history[-1] == "P":
            move = "S"
        elif opponent_history[-1] == "S":
            move = "R"

    # Strategy for Marry
    # plays the move that counters the player's most frequent move
    if len(opponent_history) >= 1:
        most_frequent = max(set(opponent_history), key=opponent_history.count)
        if most_frequent == "R":
            move = "P"
        elif most_frequent == "P":
            move = "S"
        elif most_frequent == "S":
            move = "R"

    return move
