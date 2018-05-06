#upload csv file and return a dictionary list
import csv


with open('soccer_players.csv', newline='') as csvfile:
    artreader = csv.DictReader(csvfile)
    print(artreader)
    rows = list(artreader)
    #for row in rows:


def team_sorter_experienced(players):
    tmpList = []
    for player in players:
        if player['Soccer Experience'] == 'YES':
            tmpList.append(player)

    return tmpList

def team_sorter(players):
    tmpList = []
    for player in players:
        if player['Soccer Experience'] == 'NO':
            tmpList.append(player)

    return tmpList


def team_spliter(players):
    team1=[]
    team2=[]
    team3=[]
    pick = 1
    for player in players:
        pick = pick + 1
        if pick == 1:
            team1.append(player)
        elif pick == 2:
            team2.append(player)
        elif pick == 3:
            team3.append(player)
            pick = 0

    return team1,team2,team3




var = team_sorter_experienced(rows)
var2 = team_sorter(rows)

for t in var:
    print(t)
print("\n\n\n\n\n")
for t in var2:
    print(t)

print("\n\n\n\n\n")

raptor,babies,gogo = team_spliter(var)

for player in raptor:
 print(player['Name'])
print("\n\n\n\n\n")
for player in babies:
    print(player['Name'])
print("\n\n\n\n\n")
for player in gogo:
 print(player['Name'])


with open('team1.txt', 'w') as txtfile:
    fieldnames = ['Name','Height (inches)','Soccer Experience','Guardian Name(s)']
    teamWriter = csv.DictWriter(txtfile,fieldnames)
    teamWriter.writeheader()
    for p in raptor:
        teamWriter.writerow(p)




