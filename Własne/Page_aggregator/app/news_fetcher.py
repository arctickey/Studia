import requests
from bs4 import BeautifulSoup
from app import app, db
from app.models import Content
# from app import celery
from datetime import datetime


def interia():
    page = requests.get('https://www.interia.pl/')
    soup = BeautifulSoup(page.content, 'html.parser')
    clas = soup.find('section', class_='news-section')
    a = clas.find_all('a')
    titles = [a[i].get('title') for i in
              range(app.config['START_INDEX_INTERIA'], app.config['START_INDEX_INTERIA'] + app.config["LENGTH"])]
    links = [a[i].get('href') for i in
             range(app.config['START_INDEX_INTERIA'], app.config['START_INDEX_INTERIA'] + app.config["LENGTH"])]
    for i in range(10):
        con = Content(page='interia', link=links[i], title=titles[i], time=datetime.now(),type='news')
        db.session.add(con)
    db.session.commit()

def gazeta():
    page = requests.get("https://www.gazeta.pl/0,0.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    clas = soup.find('section', class_='c-section--news-feed')
    a = clas.find_all('a')
    titles = [a[i].get('title') for i in
              range(app.config['START_INDEX_GAZETA'], app.config['START_INDEX_GAZETA'] +7)]
    links = [a[i].get('href') for i in
             range(app.config['START_INDEX_GAZETA'], app.config['START_INDEX_GAZETA'] +7)]
    for i in range(7):
        con = Content(page='gazeta', link=links[i], title=titles[i], time=datetime.now(),type='news')
        db.session.add(con)
    db.session.commit()

def bbc():
    page = requests.get('https://www.bbc.com/news')
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a', {'class': 'gs-c-promo-heading'})
    titles = [links[i].text for i in range(1, 11)]
    links = ["https://www.bbc.com" + links[i]['href'] for i in range(1, 11)]
    for i in range(10):
        con = Content(page='bbc', link=links[i], title=titles[i], time=datetime.now(),type='news')
        db.session.add(con)
    db.session.commit()


