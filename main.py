import tbapiv3

key = "jumLDLy3CyCQayvgkyFBhCgyQDg4ah8CI4EsURKAz2cw3wkHhmYucuUzBgktyfiX"

tba = tbapiv3.TBA(key)

# Use the TBA Cache (thanks Tim!!!). See cache.py. Make sure you start it before running this script.
tba.URL_PRE = 'http://localhost:8080/'

print(tba.team_matches(1986, year=2018))
