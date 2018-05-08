import csv
import datetime
import data_functions

#main script
if __name__ == "__main__":
    welcome = "Hello welcome to the League Builder v.1.0 if you want to generate 3 teams based of the csv file provided press Y\n"
    welcome2 = "or you can press any other button to exit\n"

    while True:
        reply = input(welcome+welcome2)
        if reply.lower() == "y":
            print("hi")

            players = data_functions.load_csv_file()

            experienced_players = data_functions.team_sorter_experienced(players)
            non_experienced_players = data_functions.team_sorter(players)

            raptors, sharks, dragons = data_functions.team_spliter(experienced_players, non_experienced_players)

            data_functions.write_teams_to_text(raptors, sharks, dragons)

            print("file teams.txt generated into this folder folder")

        else:
            break

        reply2 = input("enter Y if do you wish to generate info letters for all the players guardians\n")
        if reply2.lower() == "y":
            data_functions.Letters_to_teams_gurdians(raptors, sharks, dragons)
            print("letters have been generated successfully")
            break
        else:
            break