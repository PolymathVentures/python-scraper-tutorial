import requests, bs4
from bs4 import BeautifulSoup
import csv

f = open('movies.csv', 'w')
writer = csv.writer(f)

header = ['Title','ReleaseDate','Rating']
writer.writerow(header)

url = 'https://www.imdb.com/chart/top/'
page = requests.get(url)
format_page = BeautifulSoup(page.content, 'html.parser')
tbody = format_page.find('tbody', class_='lister-list')

for movie in tbody.find_all('tr'): 
    title = movie.find('td', class_='titleColumn').a.text
    year = movie.find('td', class_='titleColumn').span.text
    rating = movie.find('td', class_='ratingColumn').strong.text
    writer.writerow([title,year,rating])

f.close