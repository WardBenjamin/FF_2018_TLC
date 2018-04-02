import tbapiv3
import csv
import datetime
from slff_record import SLFFRecord

key = "jumLDLy3CyCQayvgkyFBhCgyQDg4ah8CI4EsURKAz2cw3wkHhmYucuUzBgktyfiX"

tba = tbapiv3.TBA(key)

# Use the TBA Cache (thanks Tim!!!). See cache.py. Make sure you start it before running this script.
tba.URL_PRE = 'http://localhost:8080/'

today = datetime.datetime.now().strftime("%Y-%m-%d")

# districts = tba.districts(2018)

districts = {'2018isr'}

for district in districts:
    key = district

    print("District running: " + str(key))
    rankings = tba.district_rankings(key)
    print(rankings)

    with open('output/' + str(key) + '.csv', 'w+') as f:
        writer = csv.writer(f)

        writer.writerow(["Team", "Score", "Ranking Points", "Wins", "Losses", "Awards"])

        for ranking in rankings:
            team = int(ranking.team_key[3:])  # Cut off the 'frc' prefix

            # print(tba._get('team/%s/events' % tba.team_key(team)))
            # events = tba.team_events(team, year=2018)
            # played_event_count = 0

            # for event in events:
            # if event.district is not None:
            # if key == event.district.key and event.end_date < today:
            # played_event_count += 1

            record = SLFFRecord.get_for_year(tba, team, 2018)

            # if played_event_count < 2:
            writer.writerow([team, record.score, ranking.point_total, record.wins, record.losses, record.awards])
