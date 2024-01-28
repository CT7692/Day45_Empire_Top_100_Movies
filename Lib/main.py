######   SOURCE: https://www.empireonline.com/movies/features/best-movies-2/

import requests
from bs4 import BeautifulSoup

def get_top_100_movies(my_file):
    response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
    soup = BeautifulSoup(response.text, "html.parser")
    movie_list = soup.select(".listicleItem_listicle-item__title__BfenH")
    movie_list.reverse()
    title_list = [my_file.write(f"{movie.getText()}\n") for movie in movie_list]
    return title_list

with open("empire_top_100_movies.txt", mode="w") as file:
    top_100_movies = get_top_100_movies(file)
