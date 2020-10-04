class Fixture:

    def __init__(self, team1_name, team2_name, score_home, score_away, fixture_id = None):
        self.team1_name = team1_name
        self.team2_name = team2_name
        self.score_home = score_home
        self.score_away = score_away
        self.fixture_id = fixture_id
    
    # This fucntion will take teams from the user defined Team list (team1_name, team2_name) and create a fixture list where every team plays every other team.
    # The User will input the score of each fixture and store the list for later editing/completion
    #  
    
    
