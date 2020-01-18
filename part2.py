# PART 2

import pandas as pd
import json
import sys

def part2():

    # check for acceptable number of command line args
    if len(sys.argv) != 2:
        print('ERROR: Invalid Number of Arguments')
        return
    else:
        path = sys.argv[1]

    # load business.json file to pandas dataframe
    d=[]
    for l in open(path+"business.json").readlines():
        d.append(json.loads(l))
    df = pd.DataFrame.from_records(d)

    # Filter for business in Arizona
    df = df[df['state'] == 'AZ']

    # Convert city column to lowercase
    df['city'] = df['city'].str.lower()
    df = df[df.city != '']
    df = df[df.city != 'arizona']
    df = df[df.city != 'az']
    df['city'] = df['city'].str.replace(',', '')
    df['city'] = df['city'].str.replace('.', '')
    df['city'] = df['city'].str.replace('az', '')
    df['city'] = df['city'].str.replace('  ', ' ')
    df['city'] = df['city'].str[0:-1] + df['city'].str[-1].replace(' ', '')

    # Clean misspelled cities
    df['city'] = df['city'].str.replace('phx', 'phoenix')
    df['city'] = df['city'].str.replace('north phoenix', 'phoenix')
    df['city'] = df['city'].str.replace('phoeniix', 'phoenix')
    df['city'] = df['city'].str.replace('metro phoenix', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix metro area', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix valley', 'phoenix')
    df['city'] = df['city'].str.replace('central', 'phoenix')
    df['city'] = df['city'].str.replace('central city', 'phoenix')
    df['city'] = df['city'].str.replace('phoneix', 'phoenix')
    df['city'] = df['city'].str.replace('phoniex', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix city', 'phoenix')
    df['city'] = df['city'].str.replace('phoenx', 'phoenix')
    df['city'] = df['city'].str.replace('pheonix', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix city', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix city village', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix village', 'phoenix')
    df['city'] = df['city'].str.replace('phoenix foothills village', 'phoenix')
    df['city'] = df['city'].str.replace('ahwahtukee', 'phoenix')
    df['city'] = df['city'].str.replace('ahwatukee', 'phoenix')
    df['city'] = df['city'].str.replace('ahwatukee foothills village', 'phoenix')

    df['city'] = df['city'].str.replace('old town scottsdale', 'scottsdale')
    df['city'] = df['city'].str.replace('scottsale', 'scottsdale')
    df['city'] = df['city'].str.replace('old scottsdale', 'scottsdale')
    df['city'] = df['city'].str.replace('north scottsdale', 'scottsdale')
    df['city'] = df['city'].str.replace('westworld scottsdale', 'scottsdale')
    df['city'] = df['city'].str.replace('scottdale', 'scottsdale')
    df['city'] = df['city'].str.replace('scotesdale', 'scottsdale')
    df['city'] = df['city'].str.replace('scotsdale', 'scottsdale')
    df['city'] = df['city'].str.replace('schottsdale', 'scottsdale')

    df['city'] = df['city'].str.replace('chandler-gilbert', 'chandler')
    df['city'] = df['city'].str.replace('chander', 'chandler')
    df['city'] = df['city'].str.replace('\u200bchandler', 'chandler')

    df['city'] = df['city'].str.replace('mesa arizona', 'mesa')
    df['city'] = df['city'].str.replace('east mesa', 'mesa')

    df['city'] = df['city'].str.replace('litchfield', 'litchfield park')
    df['city'] = df['city'].str.replace('park park', 'park')

    df['city'] = df['city'].str.replace('suprise', 'surprise')
    df['city'] = df['city'].str.replace('surprise crossing', 'surprise')

    df['city'] = df['city'].str.replace('cave creek road', 'cave creek')

    df['city'] = df['city'].str.replace('suncity', 'sun city')
    df['city'] = df['city'].str.replace('sun city west', 'sun city')

    df['city'] = df['city'].str.replace('fountain hls', 'fountain hills')

    df['city'] = df['city'].str.replace('laveen village', 'laveen')
    df['city'] = df['city'].str.replace('san tan', 'san tan valley')
    df['city'] = df['city'].str.replace('valley valley', 'valley')
    df['city'] = df['city'].str.replace('valley valley', 'valley')

    df['city'] = df['city'].str.replace('glbert', 'gilbert')
    df['city'] = df['city'].str.replace('gelndale', 'glendale')

    df['city'] = df['city'].str.replace('', '')
    df['city'] = df['city'].str.replace('', '')
    df['city'] = df['city'].str.replace('', '')
    df['city'] = df['city'].str.replace('', '')


    lst = list(df['city'].unique())
    print(lst)
    print(len(lst))
    return df


if __name__ == "__main__": 
    part2()
else: 
    print("Executed when imported")

