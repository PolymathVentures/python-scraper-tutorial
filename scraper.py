import requests, bs4
from bs4 import BeautifulSoup
import csv

header = ["Title", "ReleaseDate", "Rating"]
url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

root = BeautifulSoup(response.content, "html.parser")
rows = root.select("tbody.lister-list tr")

with open("movies.csv", "w") as f:

    writer = csv.writer(f)
    writer.writerow(header)

    for movie in rows:
        title = movie.select_one(".titleColumn a").text
        year = movie.select_one(".titleColumn span").text
        rating = movie.select_one(".ratingColumn strong").text

        writer.writerow([title, year, rating])
