#try:
from ossapi import Ossapi

maps = []
map_IDs = []
with open("map list.txt", "r") as file:
    round = file.readline().strip()
    maps = file.readline().replace(" ", "").split(",")
    map_IDs = [int(x) for x in file.readline().replace(" ", "").split(",")]

MPs = []
with open("MP links.txt", "r") as file:
    for line in file.readlines():
        if line != "\n":
            MPs.append(int(line.split("/")[-1]))

credentials = {}
with open("api.txt", "r") as file:
    for line in file:
        key, value = line.strip().split(' = ')
        credentials[key] = value
api = Ossapi(credentials.get('client ID'), credentials.get('client secret'))

scores = {}

for m in map_IDs:
    scores[m] = []


num_of_lobbies = len(MPs)
counter = 1
for mp in MPs:
    print(f'\r({counter}/{num_of_lobbies})', end='', flush=True)
    lobby = api.match(mp)
    for event in lobby.events:
        if event.game != None and event.game.end_time != None:
            current_map = event.game.beatmap_id
            for score in event.game.scores:
                if current_map in scores:
                    scores[current_map].append(score.score)
    counter += 1

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter

def thousands_formatter(x, pos):
    if x >= 1e3:
        return f'{x*1e-3:.0f}k'
    else:
        return f'{x:.0f}'

plt.boxplot(scores.values(), labels=maps)

plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.title(round)
plt.show()
'''except Exception as e:
    print(e)
    input("Press Enter to exit..")'''