import requests, bs4
from bs4 import BeautifulSoup
import csv

attrs_selectors = {
    "Title": ".titleColumn a",
    "ReleaseDate": ".titleColumn span",
    "Rating": ".ratingColumn strong",
}

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

root = BeautifulSoup(response.content, "html.parser")
rows = root.select("tbody.lister-list tr")

with open("movies.csv", "w") as f:

    writer = csv.DictWriter(f, fieldnames=attrs_selectors.keys())
    writer.writeheader()

    for row in rows:

        movie = {}
        for attr, selector in attrs_selectors.items():
            movie[attr] = row.select_one(selector).text

        writer.writerow(movie)
