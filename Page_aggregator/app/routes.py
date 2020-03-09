from app import app, db, news_fetcher, sport_fetcher
from flask import render_template
from app.models import Content
from datetime import datetime,timedelta


@app.route('/')
@app.route('/index')
def index():
    if not db.session.query(Content).filter_by(type='news'):
        news_fetcher.interia()
        news_fetcher.gazeta()
        news_fetcher.bbc()
    try:
        last = Content.query.with_entities(Content.time).filter_by(type='news')[0][0]
    except:
        last = None
    if last and  last + timedelta(minutes=60) > datetime.now():
        content_interia = Content.query.filter_by(page='interia', type='news').order_by(Content.time).limit(10).all()
        content_gazeta = Content.query.filter_by(page='gazeta', type='news').order_by(Content.time).limit(7).all()
        content_bbc = Content.query.filter_by(page='bbc', type='news').order_by(Content.time).limit(10).all()
    else:
        news_fetcher.interia()
        news_fetcher.gazeta()
        news_fetcher.bbc()
        content_interia = Content.query.filter_by(page='interia',type='news').order_by(Content.time).limit(10).all()
        content_gazeta = Content.query.filter_by(page='gazeta',type='news').order_by(Content.time).limit(7).all()
        content_bbc = Content.query.filter_by(page='bbc',type='news').order_by(Content.time).limit(10).all()
    return render_template('index.html',content_gazeta = content_gazeta,
                           content_interia=content_interia,content_bbc=content_bbc)

@app.route('/sport')
def sport():
    if not db.session.query(Content).filter_by(type='sport'):
        #sport_fetcher.interia()
        sport_fetcher.gazeta_sport()
        sport_fetcher.bbc_sport()
    try:
        last = Content.query.with_entities(Content.time).filter_by(type='sport')[0][0]
    except:
        last = None
    if last and last + timedelta(minutes=60) > datetime.now():
        #content_interia = Content.query.filter_by(page='interia', type='news')
        content_gazeta_sport = Content.query.filter_by(page='gazeta', type='sport').order_by(Content.time).limit(10).all()
        content_bbc_sport = Content.query.filter_by(page='bbc', type='sport').order_by(Content.time).limit(8).all()
    else:
        #fetcher.interia()
        sport_fetcher.gazeta_sport()
        sport_fetcher.bbc_sport()
        #content_interia = Content.query.filter_by(page='interia', type='news')
        content_gazeta_sport = Content.query.filter_by(page='gazeta', type='sport').order_by(Content.time).limit(10).all()
        content_bbc_sport = Content.query.filter_by(page='bbc', type='sport').order_by(Content.time).limit(8).all()
    return render_template('sport.html', content_gazeta_sport=content_gazeta_sport,content_bbc_sport=content_bbc_sport)
