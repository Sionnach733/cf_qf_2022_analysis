import requests
import csv
import pandas as pd

def fetch_semi_competitor_ids(url, csv_file):
    page_data = requests.get(url).json()
    total_pages = page_data['pagination']['totalPages']
    print('total pages: ' + str(total_pages))
    athletes = []
    for athlete in page_data['leaderboardRows']:
        athletes.append({'id': athlete['entrant']['competitorId'], 'name': athlete['entrant']['competitorName']})

    csv_columns = ['id', 'name']
    try:
        with open(csv_file, 'w', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in athletes:
                writer.writerow(data)
    except IOError:
        print("I/O error")
    print('DONE_________________________________________________________________________________')

    df = pd.read_csv(csv_file)
    df.to_csv(csv_file, index=False)


if __name__ == '__main__':
    fetch_semi_competitor_ids("https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=206&division=1&sort=0", "maleCopa.csv")

    # atlas
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=204&division=1&sort=0
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=204&division=2&sort=0

    # granite male
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=203&division=1&sort=0

    # granite female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=203&division=2&sort=0

    # far east males
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=202&division=1&sort=0

    # far east females
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=202&division=2&sort=0

    # lowlands female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=196&division=2&sort=0

    # lowlands male
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=196&division=1&sort=0

    # syndacate female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=195&division=2&sort=0

    # syndacate male
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=195&division=1&sort=0

    # torian female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=197&division=2&sort=0

    # torian male
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=197&division=1&sort=0

    # sid female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=205&division=2&sort=0

    # macc male
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=198&division=1&sort=0

    # macc female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=198&division=2&sort=0

    # cape town male
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=199&division=1&sort=0

    # cape town female
    # https://c3po.crossfit.com/api/competitions/v2/competitions/semifinals/2022/leaderboards?semifinal=199&division=2&sort=0

