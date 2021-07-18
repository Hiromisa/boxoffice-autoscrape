#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.boxofficemojo.com/weekly/?ref_=bo_nb_ml_secondarytab'
df = pd.io.html.read_html(url)

df = df[0]

df = df.drop(columns=['Genre','Budget','Running Time']).rename(columns={'%± LW' : 'Top10 Gross Change','%± LW.1' : 'Overall Grross Change'}) 

df.to_csv('WeeklyBoxoffice.csv', index=False)