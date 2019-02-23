import requests
from bs4 import BeautifulSoup
import csv


def getHtml(url):
    try:
        r= requests.get(url)
        r.raise_for_status()
        return r.text
    except:
        print("异常")


def getText(html):
    soup = BeautifulSoup(html,"html.parser")
    soup.prettify()
    tag = soup.find(class_="screening-bd")
    n = []
    for i in tag.find_all("li"):
        n.append(i.get("data-title"))
        n.append(i.get("data-release"))
        n.append(i.get("data-rate"))
        n.append(i.get("data-trailer"))
        n.append(i.get("data-duration"))
        n.append(i.get("data-region"))
        n.append(i.get("data-director"))
        n.append(i.get("data-actors"))
        while None in n:
            n.remove(None)
    step = int(8)
    movies = [n[i:i+step] for i in range(0, int(len(n)), step)]
    for x in movies:
        if x[2] =="":
            x[2] = "尚未获得评分"

    print(movies)
    return movies


def saveMovies(movies):
    csvfile = open('movies.csv', 'w', newline="")
    writer = csv.writer(csvfile)
    for movie in movies:
        writer.writerow(movie)
    csvfile.close()
    return writer



def main():
    url = "https://movie.douban.com/"
    html = getHtml(url)
    movies = getText(html)
    file = saveMovies(movies)


main()