import requests
from datetime import datetime

fromdate = str(int(datetime.timestamp((datetime(2022, 5, 21)))))
todate = str(int(datetime.timestamp(datetime.now())))
url = 'https://api.stackexchange.com/2.3/questions'
params = {'fromdate': fromdate, 'todate' : todate, 'order' : 'desc', 'sort' : 'activity' ,
          'filter' : 'default', 'site' : 'stackoverflow', 'tagged' : 'python'}
response = requests.get(url, params=params)
for item in response.json()['items']:
    print(f'{item["title"]}')
