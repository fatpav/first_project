import operator
def fixtures(teams):
    if len(teams) % 2:
        teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

    rotation = list(teams)       # copy the list

    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return fixtures

# demo code
teams = ["Liverfool", "Pressed On", "Bumville", "Spooner", "Hateford"]

# for one match each - use this block only
matches = fixtures(teams)
for f in matches:    
    print(matches)

