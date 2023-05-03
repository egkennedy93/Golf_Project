
# grab the teetime PK
# get all the bets associated with that tee time
# start processing

# for each bet
    # determine the bet type (vs player or vs team)
    # determine if its a inter-teetime bet, or a external bet (from the same day)

    # if the submitter is not in the tee time
        # check if both rounds are compelete
        # if both teetimes are complete
            # if bet type is against a Player
                # lookup both players final net score for the associated teetime. Compare the scores
                # whoever is the winner, grab that player and update their bet_winnings attribute
                # update the bet entry to be marked as closed, and set the winner field to the winner's ID
        # if one of the rounds is still being played, don't do anything

    # else 
        # if bet type is against a Player
            # lookup both players final net score for the associated teetime. Compare the scores
            # whoever is the winner, grab that player and update their bet_winnings attribute
            # update the bet entry to be marked as closed, and set the winner field to the winner's ID
        # if bet type is against the team
            # grab the players for each team
            # get their associated net scores
            # compare the team scores
            # whoever is the winner, grab that player and update their bet_winnings attribute
            # update the bet entry to be marked as closed, and set the winner field to the winner's ID



