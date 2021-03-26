import data as data
import requests
from bs4 import BeautifulSoup
import json
import re
from ast import literal_eval
import js2xml
from itertools import repeat
from pprint import pprint as pp
import pandas as pd
counter = 0
cases = []
categories = []

URL = 'https://www.worldometers.info/coronavirus/country/malaysia/'
parsed_html = requests.get(URL)
soup = BeautifulSoup(parsed_html.content, "html.parser")
overalldata = soup.find_all("div",class_="maincounter-number")

print("Total Cases: ", overalldata[0].text.strip())
print("Total Deaths: ", overalldata[1].text.strip())
print("Total Recovered: ", overalldata[2].text.strip())

scripts = soup.find("script", text=re.compile('Highcharts.chart')).text
print(scripts)
parsed = js2xml.parse(scripts)
data = [d.xpath("//property[@value='data']") for d in parsed.xpath("//property[@name='data']")]
cases = parsed.xpath("//property[@value='data']//string/text()"[0])
categories = parsed.xpath("//property[@name='categories']//string/text()"[0])
df = pd.DataFrame(cases)














