import math

def main():
    ratings_dict = {'Brumbies': 5.059261102456964, 'Sharks': -9.621951624350089, 'Cheetahs': -11.17409972773983, 'Stormers': 1.0547771464194784, 'Highlanders': 4.249399935150898, 'Crusaders': 15.138913239214475, 'Lions': -3.514220506823066, 'Reds': -12.340940348226978, 'Hurricanes': 7.9695633046844705, 'Bulls': 1.9242837734399998, 'Rebels': -7.214562417591698, 'Chiefs': 1.811153828342562, 'Force': -2.510889352631091, 'Waratahs': 8.994817833959013, 'Blues': 0.17449381369488898}
    the_round = int(input("What round is it?: "))
    matches_in_rd = int(input("How many matches in the round?: "))
    i = 0
    prediction = 0
    while i < matches_in_rd:
        team_pair = get_teams()
        home_team = team_pair[0]
        away_team = team_pair[1]
        prediction += update_ratings(ratings_dict, home_team, away_team)
        i += 1
    print("The new ratings are")
    print(ratings_dict)
    percent_acc = round((prediction/matches_in_rd)*100,1)
    print("There were " + str(matches_in_rd) + " matches in round " + str(the_round) + ", of which " + str(prediction) + " were correct.")
    print("Round Accuracy: " + str(percent_acc) + "%")


def get_teams():
    home_team = input("Enter home team: ")
    away_team = input("Enter away team: ")
    return [home_team, away_team]
    
def update_ratings(ratings_dict, home_team, away_team):
    sign = lambda x: math.copysign(1, x)
    alpha = 0.24
    home_adv = 5.14
    
    home_rating = ratings_dict[home_team]
    away_rating = ratings_dict[away_team]
    
    predicted_margin = home_rating + home_adv - away_rating
    print("The " + home_team + " have a rating of " + str(round(home_rating, 4)))
    print("The " + away_team + " have a rating of " + str(round(away_rating, 4)))
    if predicted_margin > 0:
        print("The " + home_team + " are predicted to win by " + str(abs(round(predicted_margin,0)))  + " points")
    elif predicted_margin <0:
        print("The " + away_team + " are predicted to win by " + str(abs(round(predicted_margin,0))) + " points")
    else:
        print("There is a draw predicted between the home team and the away team")

    home_score = int(input("Enter the score for the home team: "))
    away_score = int(input("Enter the score for the away team: "))

    actual_margin = home_score - away_score
    prediction_count = 0
    if sign(actual_margin) == sign(predicted_margin):
        print("The prediction was CORRECT")
        prediction_count += 1
    else:
        print("The prediction was INCORRECT")
       
    if actual_margin > 0:
        print("The " + home_team + " won this match by " + str(abs(actual_margin)))
    elif actual_margin < 0:
        print("The " + away_team + " won this match by " + str(abs(actual_margin)))
    else:
        print("This match was a draw.")
        
    updated_home_rating = home_rating + (alpha*(actual_margin - predicted_margin))
    updated_away_rating = away_rating - (alpha*(actual_margin - predicted_margin))
    print("The " + home_team + " now have a rating of " + str(round(updated_home_rating,4)))
    print("The " + away_team + " now have a rating of " + str(round(updated_away_rating,4)))
    print(" ")

    ratings_dict[home_team] = updated_home_rating
    ratings_dict[away_team] = updated_away_rating

    print(str(prediction_count))
    return prediction_count
    

main()
