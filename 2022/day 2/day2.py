input = open("input.txt", "r")
txt = input.read()

strategy_guide = txt.split("\n")

input.close()


#Opponent's moves: Rock, Paper, Scissors = "A", "B", "C"
#Your moves: Rock, Paper, Scissors = "X", "Y", "Z"
#Rock, Paper, Scissors = 1pt, 2pts, 3pts
#Win, Lose, Draw = 6pts, 0pt, 3pts

def game():

    score = 0

    for round in strategy_guide:
        if round[0] == "A":
            score += play_rock(round[-1])
        elif round[0] == "B":
            score += play_paper(round[-1])    
        elif round[0] == "C":
            score += play_scissors(round[-1])

    return f'the end result was {score}'

#It is crucial to remember, in this specific set of functions, that the first column (round[0]) is *you opponent*

def play_rock(response):
    #That's a draw (3pts) with rock (1pt)
    if response == "X":
        return 3 + 1 
    
    #That's a win (6pt) with paper (2pt)
    elif response == "Y":
        return 6 + 2
            
    #That's a loss (0pt) with scissors (3pts)
    elif response == "Z":
        return 0 + 3

def play_paper(response):    
    #That's a loss (0pt) with rock (1pt)
    if response == "X":
        return 0 + 1

    #That's a draw (3pts) with paper (2pts)
    elif response == "Y":
        return 3 + 2

    #That's a win (6pts) with scissors (3pts)
    elif response == "Z":
        return 6 + 3

def play_scissors(response):
    #That's a win (6pts) with rock (1pt)
    if response == "X":
        return 6 + 1

    #That's a loss (0pt) with paper (2pts)
    elif response == "Y":
        return 0 + 2

    #That's a draw (3pts) with scissors (3pts)
    elif response == "Z":
        return 3 + 3


game()
