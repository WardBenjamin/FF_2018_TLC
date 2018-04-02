import tbapiv3


class SLFFRecord:
    def __init__(self, _wins, _losses, _ties, _score, _awards):
        self.wins = _wins
        self.losses = _losses
        self.ties = _ties
        self.score = _score
        self.awards = _awards

    @staticmethod
    def get_for_year( tba: tbapiv3.TBA, _team, year):

        team_key = tba.team_key(_team)

        events = tba.team_events(_team, year, keys=True)

        print(events)

        _wins = 0.0
        _losses = 0.0
        _ties = 0.0

        for ekey in events:
            # print(ekey)
            # if ekey is '2017cc':
            # print(tba._fetch('event/%s/rankings' % ekey))

            try:
                rankings = tba.event_rankings(ekey).rankings

                # print(rankings)

                if rankings is None:
                    continue

                rank = next(filter(lambda ranking: ranking['team_key'] == team_key, rankings), None)

                if rank is None:
                    continue

                _record = rank['record']

                _wins += _record['wins']
                _losses += _record['losses']
                _ties += _record['ties']

            except:
                continue

        _total_relevant_matches = _wins + _losses

        _adjusted_wins = float(_wins) if _wins > 0 else 1.0
        _adjusted_losses = float(_losses) if _losses > 0 else 1.0

        _overall_score = _total_relevant_matches / (_adjusted_losses / _adjusted_wins)

        awards_list = tba.team_awards(_team, year)
        awards = ""
        for award in awards_list:
            try:
                award_name = (award['name'].split("Award")[0]).strip()
            except:
                continue
            awards += award_name + ";"

        return SLFFRecord(_wins, _losses, _ties, _overall_score, awards)
