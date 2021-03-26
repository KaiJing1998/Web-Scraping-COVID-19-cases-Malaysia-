import requests
from bs4 import BeautifulSoup
import json
import js2xml
from pandas import DataFrame
import pandas as pd

def scrape(country):
    url = 'https://www.worldometers.info/coronavirus/country/' + country + '/'
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    scripts = soup.find_all('script')
    counter = 0
    retlist = [ ]
    retlist.append(country)
    while counter < len(scripts):
        try:

            if js2xml.parse(scripts[counter].string).xpath('//property[@name="title"]//string/text()')[0] in ['Total Cases', 'Daily New Cases', '3-day moving average', 'Active Cases',
                'Total Deaths','Daily Deaths','3-day moving average','7-day moving average']:
                retlist.append(js2xml.parse(scripts[counter].string).xpath('//property[@name="title"]//string/text()')[0])
                retlist = retlist + json.loads('[' + scripts[counter].string.split('data: [', 1)[1].split(']', 1)[0] + ']')
                print(pd.DataFrame(retlist))
        except:
            pass
        counter = counter + 1
    return retlist

countries = ['Malaysia']
for country in countries:
    print(scrape(country))

# write csv file / create a csv file
# na_rep = Handling Missing Values
covid = pd.DataFrame(scrape(country))
covid.to_csv('covid-19.csv', index= False, na_rep='Unknown')
print(covid)