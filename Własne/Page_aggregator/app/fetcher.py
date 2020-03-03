import requests
from bs4 import BeautifulSoup
from app import app,db
from app.models import Content
#from app import celery

def helper():
    page = requests.get('https://www.interia.pl/')
    soup = BeautifulSoup(page.content, 'html.parser')
    clas = soup.find('section', class_='news-section')
    a = clas.find_all('a')
    titles = [a[i].get('title') for i in
              range(app.config['START_INDEX_INTERIA'], app.config['START_INDEX_INTERIA'] + app.config["LENGTH"])]
    links = [a[i].get('href') for i in
             range(app.config['START_INDEX_INTERIA'], app.config['START_INDEX_INTERIA'] + app.config["LENGTH"])]
    for i in range(10):
        con = Content(page='interia', link=links[i], title=titles[i])
        db.session.add(con)
    db.session.commit()
