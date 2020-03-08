import requests
from bs4 import BeautifulSoup
from app import app, db
from app.models import Content
# from app import celery
from datetime import datetime

def gazeta_sport():
    page = requests.get("https://www.gazeta.pl/0,0.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    clas = soup.find_all('section', class_='o-section__simple-news-list')[1]
    a = clas.find_all('a')
    titles = [a[i].get('title') for i in
              range(app.config['START_INDEX_GAZETA'], app.config['START_INDEX_GAZETA'] + 10)]
    links = [a[i].get('href') for i in
             range(app.config['START_INDEX_GAZETA'], app.config['START_INDEX_GAZETA'] + 10)]
    for i in range(10):
        con = Content(page='gazeta', link=links[i], title=titles[i], time=datetime.now(), type='sport')
        db.session.add(con)
    db.session.commit()


def bbc_sport():
    page = requests.get('https://www.bbc.com/sport')
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a', {'class': 'gs-c-promo-heading'})
    titles = [links[i].text for i in range(1, 11)]
    links = ["https://www.bbc.com" + links[i]['href'] for i in range(1, 9)]
    for i in range(8):
        con = Content(page='bbc', link=links[i], title=titles[i], time=datetime.now(),type='sport')
        db.session.add(con)
    db.session.commit()

