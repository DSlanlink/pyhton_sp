#https://server.cbaleague.com/data/player_season?matchtypeid=1&ranktype=PointsAverage
import requests
import json
import csv

def cba_name(new_year):
    url = ["https://server.cbaleague.com/data/player_season?ranktype=PointsAverage&page={}&season=%s&matchtypeid=1".format(j) %new_year for j in range(0,21) ]
    for j in url:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
        }

        response = requests.get(j,headers = header)

        new_response = response.text

        beens = json.loads(new_response)


        new_beens = beens['data']['data']
        for i in new_beens:
            cba_name = i['CNAlias']
            new_numver = i['Number']
            new_team = i['TeamCNAlias']
            new_games = i['Games']
            new_GamesStarted = i['GamesStarted']
            new_PointsAverage = i['PointsAverage']
            su = new_FieldGoalsAttemptedAverage = i['FieldGoalsAttemptedAverage']+'-'+i['FieldGoalsAverage']
            new_FieldGoalsPercentageAverage = i['FieldGoalsPercentageAverage']
            new_ReboundsAverage = i['ReboundsAverage']
            new_AssistsAverage = i['AssistsAverage']
            new_StealsAverage = i['StealsAverage']
            new_TurnoversAverage = i['TurnoversAverage']
            new_BlockedAverage = i['BlockedAverage']
            new_PersonalFoulsAverage = i['PersonalFoulsAverage']
            new_DunksAverage = i['DunksAverage']
            new_MinutesAverage = i['MinutesAverage']

            result =cba_name, new_numver, new_team,new_games,new_GamesStarted,new_PointsAverage, su ,new_FieldGoalsPercentageAverage, new_AssistsAverage,new_StealsAverage,new_TurnoversAverage, new_BlockedAverage, new_PersonalFoulsAverage,new_DunksAverage,new_MinutesAverage

            # result = new_FieldGoalsPercentageAverage, new_AssistsAverage,new_StealsAverage,new_TurnoversAverage, new_BlockedAverage, new_PersonalFoulsAverage,new_DunksAverage,new_MinutesAverage
            print(result)
            try:
                with open('D:\\new_playerData.csv', 'a', newline='') as f:
                    w = csv.writer(f)
                    w.writerow(result)

            except IndexError:
                continue

a = [2020,
2019,
2018,
2017,
2016,
2015,
2014,
2013,
2012,
2011,
2010,
2009,
2008,
2007,
2006,
2005,
2004,
2003,
2002,
2001,
2000,
1999,
1998,
1997,
1996,
1995]
for i in a:
    cba_name(i)
