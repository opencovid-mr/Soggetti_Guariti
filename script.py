import requests

from datetime import datetime

url='https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/soggetti-guariti.csv'

filename='data/soggetti-guariti-'+datetime.today().strftime('%Y-%m-%d')+'.csv'

req = requests.get(url)
csv_file = open(filename, 'wb')

csv_file.write(req.content)
csv_file.close()


url='https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-second-booster.csv'

filename='data/platea-second-booster-'+datetime.today().strftime('%Y-%m-%d')+'.csv'

req = requests.get(url)
csv_file = open(filename, 'wb')

csv_file.write(req.content)
csv_file.close()


