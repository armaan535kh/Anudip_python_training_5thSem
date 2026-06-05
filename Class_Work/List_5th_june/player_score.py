player_score = []
#input of score from user

for i in range(2):
    score = int(input("Enter the score of player {} ".format(i+1)))
    player_score.append(score)

print("Score of 11 players: ", player_score)

max_score = player_score[0]

for index in range(1, len(player_score)):
    if player_score[index] > max_score:
        max_score = player_score[index]

print("The highest score is ", max_score)
