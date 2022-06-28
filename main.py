import requests
import csv
import pandas as pd


def remove_blank_rows():
    df = pd.read_csv('femaleAthletesqf.csv')
    df.to_csv('femaleAthletesqf2.csv', index=False)


def setup_data_qf(url):
    page_data = requests.get(url).json()
    total_pages = page_data['pagination']['totalPages']
    print('total pages: ' + str(total_pages))
    athletes = []
    for athlete in page_data['leaderboardRows']:
        athletes.append(curate_athlete_data_qf(athlete))

    for page in range(2, total_pages + 1):
        url = 'https://c3po.crossfit.com/api/competitions/v2/competitions/quarterfinalsindividual/2022/leaderboards' \
              '?division=2&region=0&sort=0&page='+str(page)
        page_data = requests.get(url).json()

        for athlete in page_data['leaderboardRows']:
            athletes.append(curate_athlete_data_qf(athlete))
    print(athletes)
    csv_columns = ['id', 'rank', 'name', 'gender', 'country', 'region',
                   'age', 'weight', 'height', 'QFOneScore', 'QFOneRank',
                   'QFTwoScore', 'QFTwoRank', 'QFThreeScore', 'QFThreeRank',
                   'QFFourScore', 'QFFourRank', 'QFFiveScore', 'QFFiveRank']
    csv_file = "femaleAthletesqf.csv"
    try:
        with open(csv_file, 'w', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in athletes:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    print('DONE_________________________________________________________________________________')


def setup_data_open(url):
    page_data = requests.get(url).json()
    # total_pages = 106  # females
    total_pages = 146  # males
    athletes = []
    for athlete in page_data['leaderboardRows']:
        athletes.append(curate_athlete_data_open(athlete))

    for page in range(2, total_pages + 1):
        url = 'https://c3po.crossfit.com/api/competitions/v2/competitions/open/2022/leaderboards?view=0&division=1' \
              '&region=0&scaled=0&sort=0&page='+str(page)
        page_data = requests.get(url).json()

        for athlete in page_data['leaderboardRows']:
            athletes.append(curate_athlete_data_open(athlete))
    print(athletes)
    csv_columns = ['id', 'rank', 'name', 'gender', 'country', 'region',
                   'age', 'weight', 'height', '22.1Score', '22.1Rank',
                   '22.2Score', '22.2Rank', '22.3Score', '22.3Rank']
    csv_file = "maleAthletesOpen.csv"
    try:
        with open(csv_file, 'w', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in athletes:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    print('DONE_________________________________________________________________________________')


def print_athlete_data(athlete_info_raw):
    print(athlete_info_raw['entrant']['competitorName'])
    print(athlete_info_raw['entrant']['competitorId'])
    print(athlete_info_raw['entrant']['gender'])
    print(athlete_info_raw['entrant']['countryOfOriginName'])
    print(athlete_info_raw['entrant']['regionName'])
    print(athlete_info_raw['entrant']['age'])
    print(athlete_info_raw['entrant']['height'])
    print(athlete_info_raw['entrant']['weight'])
    print(athlete_info_raw['scores'][0]['scoreDisplay'])
    print(athlete_info_raw['scores'][1]['scoreDisplay'])
    print(athlete_info_raw['scores'][2]['scoreDisplay'])
    print(athlete_info_raw['scores'][3]['scoreDisplay'])
    print(athlete_info_raw['scores'][4]['scoreDisplay'])


def curate_athlete_data_qf(athlete_info_raw):
    athlete_info_curated = {'id': athlete_info_raw['entrant']['competitorId'],
                            'rank': athlete_info_raw['overallRank'],
                            'name': athlete_info_raw['entrant']['competitorName'],
                            'gender': athlete_info_raw['entrant']['gender'],
                            'country': athlete_info_raw['entrant']['countryOfOriginName'],
                            'region': athlete_info_raw['entrant']['regionName'],
                            'age': athlete_info_raw['entrant']['age'], 'height': athlete_info_raw['entrant']['height'],
                            'weight': athlete_info_raw['entrant']['weight'],
                            'QFOneScore': athlete_info_raw['scores'][0]['scoreDisplay'],
                            'QFOneRank': athlete_info_raw['scores'][0]['rank'],
                            'QFTwoScore': athlete_info_raw['scores'][1]['scoreDisplay'],
                            'QFTwoRank': athlete_info_raw['scores'][1]['rank'],
                            'QFThreeScore': athlete_info_raw['scores'][2]['scoreDisplay'],
                            'QFThreeRank': athlete_info_raw['scores'][2]['rank'],
                            'QFFourScore': athlete_info_raw['scores'][3]['scoreDisplay'],
                            'QFFourRank': athlete_info_raw['scores'][3]['rank'],
                            'QFFiveScore': athlete_info_raw['scores'][4]['scoreDisplay'],
                            'QFFiveRank': athlete_info_raw['scores'][4]['rank']}
    return athlete_info_curated


def curate_athlete_data_open(athlete_info_raw):
    athlete_info_curated = {'id': athlete_info_raw['entrant']['competitorId'],
                            'rank': athlete_info_raw['overallRank'],
                            'name': athlete_info_raw['entrant']['competitorName'],
                            'gender': athlete_info_raw['entrant']['gender'],
                            'country': athlete_info_raw['entrant']['countryOfOriginName'],
                            'region': athlete_info_raw['entrant']['regionName'],
                            'age': athlete_info_raw['entrant']['age'], 'height': athlete_info_raw['entrant']['height'],
                            'weight': athlete_info_raw['entrant']['weight'],
                            '22.1Score': athlete_info_raw['scores'][0]['scoreDisplay'],
                            '22.1Rank': athlete_info_raw['scores'][0]['rank'],
                            '22.2Score': athlete_info_raw['scores'][1]['scoreDisplay'],
                            '22.2Rank': athlete_info_raw['scores'][1]['rank'],
                            '22.3Score': athlete_info_raw['scores'][2]['scoreDisplay'],
                            '22.3Rank': athlete_info_raw['scores'][2]['rank']}
    return athlete_info_curated


if __name__ == '__main__':
    # quarterfinals
    setup_data_qf('https://c3po.crossfit.com/api/competitions/v2/competitions/quarterfinalsindividual/2022/leaderboards'
                  '?division=2&region=0&sort=0')

    # open
    # setup_data_open('https://c3po.crossfit.com/api/competitions/v2/competitions/open/2022/leaderboards?view=0'
    #                 '&division=1&region=0&scaled=0&sort=0')
    remove_blank_rows()
