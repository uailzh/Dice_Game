import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print("Invalid integer, try again")

max_score = 50
#this statement puts 0 in the least for each player that we have
player_scores = [0 for _ in range(players)]

#will keep looping till one of the scores in list is less than the max score
while max(player_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer number ", player_index + 1, " turn just started!")
        print("Your total score is", player_scores[player_index],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll(y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1, turn is done")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)

        player_scores[player_index] += current_score
        print("Your total score is: ", player_scores[player_index])

max_score = max(player_scores)
winning_inx = player_scores.index(max_score)
print("Player number", winning_inx + 1, "won the game with a score of:", max_score)


