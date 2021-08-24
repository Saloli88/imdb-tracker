from bs4 import BeautifulSoup
import requests
from requests.exceptions import URLRequired


class IMDB(object):
    def __init__(self, url, html, soup):
        self.url = url
        self.soup = soup
        self.html = html

    def tracker(url):
        html = requests.get(url).content
        soup = BeautifulSoup(html, "lxml")
        list = soup.find("tbody", {"class": "lister-list"}).find_all("tr")
        count = 0
        for i in list:
            title = i.find("td", {"class": "titleColumn"}).find("a").text
            rating = i.find("td", {"class": "ratingColumn imdbRating"}).text.strip()
            year = i.find("td", {"class", "titleColumn"}).find("span").text.strip("()")
            count = count + 1
            print(f"{count}.{title}\nRating:{rating}\nReleased in: {year}\n")


options = [
    "Most popular movies ",
    "Top rated movies",
    "Most popular shows",
    "Top rated shows",
    "Exit the program",
]
while True:
    for i in range(len(options)):
        print(f"{i}.{options[i]}")
    choice = input("Select:")
    if choice == "0":
        IMDB.tracker("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm")
    elif choice == "1":
        IMDB.tracker("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    elif choice == "2":
        IMDB.tracker("https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv")
    elif choice == "3":
        IMDB.tracker("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")
    elif choice == "4":
        print("Closing the program")
        print("...\n...")
        break
    else:
        print("Select a number as stated below")
