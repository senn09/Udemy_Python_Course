import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = [(movie.getText().split(") ")) for movie in soup.find_all(name="h3", class_="title")]
movies = [movie[0].split(": ") if len(movie)==1 else movie for movie in movies]
movies = [[int(movie[0]), movie[1]] for movie in movies]
movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie[0]}) {movie[1]}\n")
