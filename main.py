"""Scrape the Empire magazine list of the 100 best movies and save it to a text file.

This script requests the archived web page, parses the movie titles from the HTML,
reverses the order to show the rankings from #100 to #1, and writes each title to
`movies.txt`.
"""

import requests
from bs4 import BeautifulSoup

# Archived page containing the ranked movie list.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Fetch the page content and ensure the response is decoded as UTF-8.
r = requests.get(url=URL)
r.encoding = "utf-8"
data = r.text

# Parse the HTML so we can locate each movie title.
soup = BeautifulSoup(data, "html.parser")
all_movies_name = soup.find_all(name="h3", class_="title")

# Extract the visible title text from each movie entry.
movies_list = [movie.getText() for movie in all_movies_name]

# Write the list to a file in the correct descending ranking order.
with open("movies.txt", "w") as file:
    for movie in reversed(movies_list):
        file.write(f"{movie}\n")
