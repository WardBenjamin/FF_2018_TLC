import tbapiv3
import csv

key = "jumLDLy3CyCQayvgkyFBhCgyQDg4ah8CI4EsURKAz2cw3wkHhmYucuUzBgktyfiX"

tba = tbapiv3.TBA(key)

# Use the TBA Cache (thanks Tim!!!). See cache.py. Make sure you start it before running this script.
tba.URL_PRE = 'http://localhost:8080/'

districts = tba.districts(2018)

for district in districts:
    key = district.key

    print("District running: " + str(key))
    rankings = tba.district_rankings(key)
    print(rankings)

    with open('output/' + str(key) + '.csv', 'w+') as f:
        writer = csv.writer(f)
        for ranking in rankings:
            team = ranking.team_key[3:]
            writer.writerow([team, ranking.point_total])
