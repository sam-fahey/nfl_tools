import requests, json
import numpy as np

seed_wins = {}
for i in range(16):
    seed_wins["%i"%(i+1)] = []
    
for year in range(2008, 2019):

    site = "https://www.nfl.com/standings/division/%i/REG"%year
    html = requests.get(site)
    content = str(html.content)
    standings_raw = ((content.split("teamRecords")[1][2:]).split("]")[0])+"]"
    standings_data = json.loads(standings_raw)
    
    for team in standings_data:
        wins = team["overallWin"] + 0.5*team["overallTie"]
        seed = team["conferenceRank"]
        seed_wins["%i"%seed].append(wins)
        
for seed in range(1,12):
    print(seed, np.mean(seed_wins["%i"%seed]), np.std(seed_wins["%i"%seed]))
