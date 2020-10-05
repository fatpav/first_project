class Fixture:

    def __init__(self, teams, fixture_id = None):
        self.teams = []
        self.fixture_id = id
        
    
    # This fucntion will take teams from the user defined Team list (team1_name, team2_name) and create a fixture list where every team plays every other team.
    # The User will input the score of each fixture and store the list for later editing/completion
    #  
    
    # import operator
    # def fixtures(teams):
    # if len(teams) % 2:
    #     teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

    # rotation = list(teams)       # copy the list

    # fixtures = []
    # for i in range(0, len(teams)-1):
    #     fixtures.append(rotation)
    #     rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    # return fixtures
