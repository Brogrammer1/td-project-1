# upload csv file and return a dictionary list
import csv
import datetime






# this loads the csv file and then returns it  as a list of dictionares to be assigned to a variable
def load_csv_file():
    with open('soccer_players.csv', newline='') as csvfile:
        teamreader = csv.DictReader(csvfile)
        rows = list(teamreader)
    return rows


# this accepts the list loaded from the csv file and returns a list of only the experieced players
def team_sorter_experienced(players):
    tmpList = []
    for player in players:
        if player['Soccer Experience'] == 'YES':
            tmpList.append(player)

    return tmpList


# this accepts the list loaded from the csv file and returns a list of only the non-experieced players
def team_sorter(players):
    tmpList = []
    for player in players:
        if player['Soccer Experience'] == 'NO':
            tmpList.append(player)

    return tmpList


# this accepts the lists of experiecned and non expereiced and divides them across 3 teams
def team_spliter(players_exp, players_no_exp):
    team1 = []
    team2 = []
    team3 = []
    pick = 0
    pick2 = 0
    for player in players_exp:
        pick = pick + 1
        if pick == 1:
            team1.append(player)

        elif pick == 2:
            team2.append(player)
        elif pick == 3:
            pick = 0
            team3.append(player)

    for play in players_no_exp:
        pick2 += 1
        if pick2 == 1:
            team1.append(play)
        elif pick2 == 2:
            team2.append(play)
        elif pick2 == 3:
            team3.append(play)
            pick2 = 0

    return team1, team2, team3

# this accepts the three teams and writes them to a text file
def write_teams_to_text(raptors, sharks, dragons):
    for member in raptors:
        member.pop('Height (inches)', None)
    for member in sharks:
        member.pop('Height (inches)', None)
    for member in dragons:
        member.pop('Height (inches)', None)
    with open('teams.txt', 'w') as txtfile:
        fieldnames = raptors[0].keys()
        team_name_writer = csv.writer(txtfile)

        teamwriter = csv.DictWriter(txtfile, fieldnames)

        team_name_writer.writerow(["RAPTORS"])
        team_name_writer.writerow([])
        teamwriter.writeheader()

        for member in raptors:
            teamwriter.writerow(member)

        team_name_writer.writerow([])
        team_name_writer.writerow(["SHARKS"])
        team_name_writer.writerow([])
        teamwriter.writeheader()

        for member in sharks:
            teamwriter.writerow(member)

        team_name_writer.writerow([])
        team_name_writer.writerow(["DRAGONS"])
        team_name_writer.writerow([])
        teamwriter.writeheader()

        for member in dragons:
            teamwriter.writerow(member)


#this writes the letters to the players guardians

def write_letter_to_csv(team,team_name):
    date = datetime.datetime.now()
    trainingdate = date.date() + datetime.timedelta(days=14)
    trainingtime = "2.pm"

    for member in team:
        templist = member["Name"].split(" ")
        with open("{}_{}.txt".format(templist[0].lower(), templist[1].lower()), "w+") as letter:
            letter.write("Dear {},\n\nWe are happy to announce that your child {} has been drafted to the {}.\n"
                         .format(member['Guardian Name(s)'], member['Name'], team_name))
            letter.write("We will have out first practice at Syon Park on {} at {}\n\nRegards"
                         .format(trainingdate, trainingtime))

    print("letters have been generated for the {}".format(team_name))




if __name__ == "__main__":
    #this is just test code to see if methods was fully functional, please ignore
    rows = load_csv_file()
    var = team_sorter_experienced(rows)
    var2 = team_sorter(rows)

    for t in var:
        print(t)
    print("\n\n\n\n\n")
    for n in var2:
        print(n)

    print("\n\n\n\n\n")

    raptor, sharks, dragons = team_spliter(var, var2)

    for player in raptor:
        print(player['Name'])
    print("\n\n\n\n\n")
    for player in sharks:
        print(player['Name'])
    print("\n\n\n\n\n")
    for player in dragons:
        print(player['Name'], player['Soccer Experience'])

    print(raptor)
    for p in raptor:
        for k, v in p.items():
            print(v)
    print(raptor[0].keys())




    write_teams_to_text(raptor, sharks, dragons)

    for m in raptor:
        templist = m["Name"].split(" ")
        print("{}_{}".format(templist[0].lower(), templist[1].lower()))




