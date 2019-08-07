"""
Use the football data API to get past years data
Usage:
python make_results_from_fd.py 2018
"""
import sys
from airsenal.framework.data_fetcher import *
from airsenal.framework.mappings import alternative_team_names

start_year = sys.argv[-1]
start_year_short = start_year[-2:]
end_year_short = str(int(start_year_short) + 1)
end_year = "20" + end_year_short

outfilename = "../data/results_{}{}_with_gw.csv".format(
    start_year_short, end_year_short
)
outfile = open(outfilename, "w")
outfile.write("date,home_team,away_team,home_score,away_score,gameweek\n")

home_team = ""
away_team = ""
datestr = ""

gameweek = 0
md = MatchDataFetcher()

for gw in range(1,39):
    results = md.get_results(gw, start_year)
    for result in results:
        date = result[0].split("T")[0]
        home_team = alternative_team_names[result[1]][1]
        away_team = alternative_team_names[result[2]][1]
        home_score = result[3]
        away_score = result[4]
        outfile.write("{},{},{},{},{},{}\n".format(date,
                                                   home_team,
                                                   away_team,
                                                   home_score,
                                                   away_score,
                                                   gw))
        print("{} {} {} {} {} {}".format(gw, date, home_team, away_team, home_score, away_score))
outfile.close()
