import tbapiv3
import csv
import datetime
from slff_record import SLFFRecord

key = "jumLDLy3CyCQayvgkyFBhCgyQDg4ah8CI4EsURKAz2cw3wkHhmYucuUzBgktyfiX"

tba = tbapiv3.TBA(key)

# Use the TBA Cache (thanks Tim!!!). See cache.py. Make sure you start it before running this script.
tba.URL_PRE = 'http://localhost:8080/'

today = datetime.datetime.now().strftime("%Y-%m-%d")

districts = tba.districts(2018)

# districts = {'2018isr'}

ranking_list = []

for district in districts:
    key = district.key

    print("District running: " + str(key))
    rankings = tba.district_rankings(key)
    # print(rankings)

    ranking_list.append(rankings)


with open('output/overall_rankings.csv', 'w+', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(["Team", "Ranking Points"])

    for district_rankings in ranking_list:
        for ranking in district_rankings:
            team = int(ranking.team_key[3:])  # Cut off the 'frc' prefix

            # if played_event_count < 2:
            writer.writerow([team, ranking.point_total])
