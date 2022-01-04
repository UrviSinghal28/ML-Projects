# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
#inspiration from mikw's answer on FCC forum

sequence={}

def player(prev_play, opponent_history=[]):
    n=6

    if prev_play in ["R","P","S"]:
      opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > n:
      last_n = "".join(opponent_history[-n:])

      if "".join(opponent_history[-(n+1):]) in sequence.keys():
        sequence["".join(opponent_history[-(n+1):])]+=1
    
      else:
        sequence["".join(opponent_history[-(n+1):])]=1  

      potential_plays = [
        last_n + "R",
        last_n + "P",
        last_n + "S",
    ]

      for i in potential_plays:
        if not i in sequence.keys():
          sequence[i] = 0

      predict = max(potential_plays, key=lambda key: sequence[key])

      if predict[-1] == "P":
        guess = "S"
      if predict[-1] == "R":
        guess = "P"
      if predict[-1] == "S":
        guess = "R"

    return guess
