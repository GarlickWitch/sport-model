
from elosports.elo import Elo
import pandas

# all approved uwcl matches
df = pandas.read_excel("data/uwcl.ods", engine="odf")

# make a list of all possible teams in the data set
allteams = set(df['n_HomeTeamID'].tolist() + df['n_AwayTeamID'].tolist())

# all time league and few samples so unusually high k
eloLeague = Elo(k = 60)

for team in allteams:
	eloLeague.addPlayer(team)

for game in df.iterrows():
    # swap points based on result
    if (game[1]['n_HomeGoals'] > game[1]['n_AwayGoals']):
        # winner, loser, winner played at home
        eloLeague.gameOver(game[1]['n_HomeTeamID'], game[1]['n_AwayTeamID'], True)
    elif (game[1]['n_AwayGoals'] > game[1]['n_HomeGoals']):
        # winner, loser, winner played away
        eloLeague.gameOver(game[1]['n_AwayTeamID'], game[1]['n_HomeTeamID'], False)
 
# rank based on elo points
v = sorted(eloLeague.ratingDict.items(), key=lambda item: item[1])

print(v)