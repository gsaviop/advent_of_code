from day2 import strategy_guide

lose, draw, win = "X", "Y", "Z"
rock, paper, scissors = "A", "B", "C"

#Rock, Paper, Scissors -> 1pt, 2pts, 3pts
#Win, Lose, Draw -> 6pts, 0pt, 3pts

def game():

    score = 0

    for round in strategy_guide:
        if round[0] == rock:
            score += play_rock(round[-1])
        if round[0] == paper:
            score += play_paper(round[-1])
        if round[0] == scissors:
            score += play_scissors(round[-1])   

    return f'the end result was {score}'

def play_rock(result):
    #To lose (0pt) against rock, you need scissors (3pts)
    if result == lose:
        return 0 + 3 
    #To draw (3pts) against rock, you need rock (1pt)
    elif result == draw:
        return 3 + 1

    #To win (6pts) against rock, you need paper (2pts)
    elif result == win:
        return 6 + 2

def play_paper(result): 
    #To lose (0pt) against paper, you need rock (1pt)
    if result == lose:
        return 0 + 1 
    #To draw (3pts) against paper, you need paper (2pts)
    elif result == draw:
        return 3 + 2

    #To win (6pts) against paper, you need scissors (3pts)
    elif result == win:
        return 6 + 3

def play_scissors(result):       
    #To lose (0pt) against scissors, you need paper (2pts)
    if result == lose:
        return 0 + 2 
    #To draw (3pts) against scissors, you need scissors (3pts)
    elif result == draw:
        return 3 + 3

    #To win (6pts) against scissors, you need rock (1pt)
    elif result == win:
        return 6 + 1


game()
