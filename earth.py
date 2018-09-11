from bs4 import BeautifulSoup
from requests import get
import pandas as pd

from time import sleep
from time import time

from random import randint
from IPython.core.display import clear_output


#### Getting years form 2010 to 2018
years_url = [str(i) for i in range(2010,2018)]

#### Monitoring loop
start_time = time()
request = 0

#### List to store data
date = []
Time = []
magnitude = []
epicenter = []

#### for every year 2010 to 2018
for year_url in years_url:

    ### requesting url
    url_response = get('http://seismonepal.gov.np/earthquakes/' + year_url)

    ### pauing loop
    sleep(randint(8,15))

    #### Monitoring request
    request += 1
    elapsed_time = time() - start_time

    clear_output(wait=True)

    #### prasing requested content with BeautifulSoup
    html_page = BeautifulSoup(url_response.text, 'html.parser')

    #### Selecting every tr in tbody
    container = html_page.tbody.find_all('tr')

    #### For every tr
    for content in container:

        ### Scrape date
        dates = content.findAll('td')[0].text
        date.append(dates)

        ### scrape time
        times = content.findAll('td')[1].text
        Time.append(times)

        ### scrape magnitude
        magnitudes = float(content.findAll('td')[4].text)
        magnitude.append(magnitudes)

        ### scrape epicenter
        epicenters = content.findAll('td')[6].text
        epicenter.append(epicenters)

### Storing Data in data frame
data = pd.DataFrame({
    'Date': date,
    'Time': Time,
    'Magnitude': magnitude,
    'Epicenter': epicenter
})

print(data.info())

path = 'C:\\Users\\Dell\\Documents\\Python-class\\project\\CSV\\'

### saving in csv format
data.to_csv(path+'EarthQuake.csv', index=False)